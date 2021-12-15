from flask import request, current_app, jsonify
from http import HTTPStatus
from app.exc import (
    InvalidCPFError, 
    InvalidDataTypeError, 
    InvalidEmailError, 
    InvalidPassword, 
    EmailVerifiedError, 
    InvalidUser,
    InvalidKey,
    UnauthorizedAccessError,
)
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.exceptions import NotFound
from datetime import datetime, timedelta
from app.services.verify_user_email import verify_user_email
from app.models.users_model import UserModel
from app.models.user_token_model import UserTokenModel


@jwt_required()
def create_basic_user():
    try:
        session = current_app.db.session

        data = request.get_json()
    
        new_user = UserModel(**data)
        
        session.add(new_user)
        session.commit()

        access_token = create_access_token(new_user, expires_delta=timedelta(minutes=30))

        found_user = UserModel.query.filter_by(email=new_user.email).first()

        if found_user:
            info_token = {
                "user_id": found_user.id,
                "token": access_token,
                "token_expire": datetime.today()
            }
        else:
            return {'error': 'Failed to find user on database.'}, HTTPStatus.NOT_FOUND

        new_user_token = UserTokenModel(**info_token)

        session = current_app.db.session

        session.add(new_user_token)
        session.commit()

        verify_user_email(new_user.name, new_user.email, access_token)

    except InvalidDataTypeError as e:
        return {"error": e.message}, e.code

    except InvalidEmailError as e:
        return {"error": e.message}, e.code

    except InvalidCPFError as e:
        return {"error": e.message}, e.code

    except IntegrityError:
        return {"error": "User already exists."}, HTTPStatus.CONFLICT

    return jsonify(new_user), HTTPStatus.CREATED


def verify_user(token):
    try:
        token = UserTokenModel.query.filter_by(token=token).first()

        if token:
            info = {"verified": True}
            user = UserModel.query.filter_by(id=token.user_id).update(info)
            current_app.db.session.commit()

        user_updated = UserModel.query.filter_by(id=token.user_id).first()
    
    except EmailVerifiedError as e:
        return {"error": e.message}, e.code
    
    return jsonify(user_updated), HTTPStatus.OK


def user_login():
    try:
        user_data = request.get_json()

        email = user_data["email"]
        password = user_data["password"]

        found_user: UserModel = UserModel.query.filter_by(
            email=email).first_or_404()

        if found_user.check_password(password):
            access_token = create_access_token(identity=found_user)
            return {"token": access_token}, HTTPStatus.OK

    except NotFound:
        return {"error": "User not found"}, HTTPStatus.NOT_FOUND

    except InvalidPassword as e:
        return {"error": e.message}, e.code


@jwt_required()
def get_one_user():
    try:
        user_token = get_jwt_identity()

        found_user: UserModel = UserModel.query.filter_by(id=user_token['id']).first_or_404()

    except NotFound:
        return {"error": "User not found"}, HTTPStatus.NOT_FOUND

    return jsonify(found_user), HTTPStatus.OK


@jwt_required()
def update_user():
    try:
        session = current_app.db.session

        user_token = get_jwt_identity()
        data = request.get_json()
        data_keys = data.keys()
        valid_keys = ["email",
                      "name",
                      "cpf",
                      "password",
                      "current_password"
                      ]
        current_password = data.pop("current_password")
        updated_user: UserModel = UserModel.query.filter_by(id=user_token['id']).first()

        if not updated_user:
            raise InvalidUser
            
        for key in data_keys:
            if key not in valid_keys:
                raise InvalidKey(key)
            if key == "password":
                if updated_user.check_password(current_password):
                    setattr(updated_user, key, data[key])
            else:
                setattr(updated_user, key, data[key])
            
        session.commit()

        found_user: UserModel = UserModel.query.filter_by(
            id=user_token['id']).first()

    except InvalidDataTypeError as e:
        return {"error": e.message}, e.code

    except InvalidEmailError as e:
        return {"error": e.message}, e.code

    except InvalidCPFError as e:
        return {"error": e.message}, e.code

    except InvalidUser as e:
        return {"error": e.message}, e.code
        
    except InvalidKey as e:
        return {"error": e.message}, e.code

    except InvalidPassword as e:
        return {"error": e.message}, e.code

    except IntegrityError:
        return {"error": "User already exists."}, HTTPStatus.CONFLICT
    
    return jsonify(found_user), HTTPStatus.ACCEPTED


@jwt_required()
def delete_user(id):
    try:
        user_logged = get_jwt_identity()
        session = current_app.db.session

        if id != user_logged['id']:
            raise UnauthorizedAccessError

        user_to_delete : UserModel = UserModel.query.filter_by(id=id).first()

        if not user_to_delete:
            raise InvalidUser

        session.delete(user_to_delete)
        session.commit()
        
    except InvalidUser as e:
        return {"error": e.message}, e.code

    except UnauthorizedAccessError as e:
        return {"error": e.message}, e.code

    return {"message": "Successfully deleted."}, HTTPStatus.OK