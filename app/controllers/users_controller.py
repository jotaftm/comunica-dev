from flask import request, current_app, jsonify
from http import HTTPStatus
from uuid import uuid4
from app.configs.decorators import verify_role_admin
from app.exc import (
    InvalidCPFError, 
    InvalidDataTypeError, 
    InvalidEmailError, 
    InvalidPassword, 
    EmailVerifiedError, 
    InvalidUser,
    InvalidKey,
    UnauthorizedAccessError,
    MandatoryKeyError,
)
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.exceptions import NotFound
from datetime import datetime, timedelta
from app.models.lessons_model import LessonModel
from app.services.verify_user_email import verify_user_email
from app.models.users_model import UserModel
from app.models.user_token_model import UserTokenModel
from app.services.reset_password import send_reset_password_code


@jwt_required()
@verify_role_admin
def list_users():
    try:
        users_list = UserModel.query.all()

    except KeyError:
        return {"error": "Invalid token."}, HTTPStatus.UNAUTHORIZED

    return jsonify(users_list), HTTPStatus.OK


# @jwt_required()
def create_basic_user():
    try:
        session = current_app.db.session

        data = request.get_json()

        invalid_keys = [
            'user_role',
            'created_at',
            'premium_at',
            'premium_expire',
            'is_premium',
            'verified',
            'password_hash']

        for key in data.keys():
            if key in invalid_keys:
                raise InvalidKey(key)

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

    except InvalidKey as e:
        return {"error": e.message}, e.code

    except IntegrityError:
        return {"error": "User already exists."}, HTTPStatus.CONFLICT

    except TypeError as e:
        return {"error": e.args[0][0:-13] + "to create a user."}, HTTPStatus.BAD_REQUEST

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
            if found_user.is_premium:
                lessons = LessonModel.query.all()
            else:
                lessons = LessonModel.query.filter_by(is_premium=False).all()

            found_user.lessons = lessons

            current_app.db.session.commit()

            access_token = create_access_token(identity=found_user)
            return {"token": access_token}, HTTPStatus.OK

    except NotFound:
        return {"error": "User not found"}, HTTPStatus.NOT_FOUND

    except InvalidPassword as e:
        return {"error": e.message}, e.code


@jwt_required()
def get_my_data():
    try:
        user_logged = get_jwt_identity()

        found_user: UserModel = UserModel.query.filter_by(id=user_logged['id']).first_or_404()

    except NotFound:
        return {"error": "User not found"}, HTTPStatus.NOT_FOUND
    
    except KeyError:
        return {"error": "Invalid token."}, HTTPStatus.UNAUTHORIZED

    return jsonify(found_user), HTTPStatus.OK


@jwt_required()
def get_one_user(id):
    try:
        user_logged = get_jwt_identity()

        if id != user_logged['id'] and user_logged['user_role'] == 'user':
            raise UnauthorizedAccessError

        found_user: UserModel = UserModel.query.filter_by(id=id).first_or_404()

    except NotFound:
        return {"error": "User not found"}, HTTPStatus.NOT_FOUND
    
    except KeyError:
        return {"error": "Invalid token."}, HTTPStatus.UNAUTHORIZED

    except UnauthorizedAccessError as e:
        return {"error": e.message}, e.code

    return jsonify(found_user), HTTPStatus.OK


@jwt_required()
def update_user(id):
    try:
        session = current_app.db.session

        user_logged = get_jwt_identity()

        if id != user_logged['id'] and user_logged['user_role'] == 'user':
            raise UnauthorizedAccessError

        data = request.get_json()
        data_keys = data.keys()
        valid_keys = ["email",
                      "name",
                      "cpf",
                      "password",
                      "current_password"
                      ]

        if not 'current_password' in data.keys():
            raise MandatoryKeyError('current_password')
        
        current_password = data.pop("current_password")
        updated_user: UserModel = UserModel.query.filter_by(id=id).first()

        if not updated_user:
            raise InvalidUser

        updated_user.check_password(current_password)

        for key in data_keys:
            if key not in valid_keys:
                raise InvalidKey(key)

            setattr(updated_user, key, data[key])
            
        session.commit()

        found_user: UserModel = UserModel.query.filter_by(
            id=id).first()

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

    except MandatoryKeyError as e:
        return {"error": e.message}, e.code

    except IntegrityError:
        return {"error": "User already exists."}, HTTPStatus.CONFLICT

    except KeyError:
        return {"error": "Invalid token."}, HTTPStatus.UNAUTHORIZED

    except UnauthorizedAccessError as e:
        return {"error": e.message}, e.code
    
    return jsonify(found_user), HTTPStatus.OK


def confirm_password_reset():
    data = request.get_json()

    try:
        if 'email' in data:
            user = UserModel.query.filter_by(email=data['email']).first_or_404()

            if user:
                reset_code = str(uuid4())[0:5]
                send_reset_password_code(user.name, user.email, reset_code)
                info = {"reset_code": reset_code}
                user_update = UserModel.query.filter_by(email=data['email']).update(info)
                current_app.db.session.commit()

                return {'msg': 'Mail sent to user successfully'}, HTTPStatus.OK

    except NotFound:
        return {"error": "Email provided does not exist"}, HTTPStatus.NOT_FOUND


def reset_user_password():
    valid_keys = ['email', 'reset_code', 'new_password']
    data = request.get_json()

    for key in data.keys():
        if key not in valid_keys or not len(data) == 3:
            return {'error': 'Wrong request'}, HTTPStatus.FORBIDDEN

    user_to_update = UserModel.query.filter_by(reset_code=data['reset_code']).first_or_404(description='User not found')

    if user_to_update:
        session = current_app.db.session
        setattr(user_to_update, 'password', data['new_password'])
        session.commit()

    return {'msg': f'User password reset successfully'}, HTTPStatus.OK


@jwt_required()
def delete_user(id):
    try:
        user_logged = get_jwt_identity()
        session = current_app.db.session

        if id != user_logged['id'] and user_logged['user_role'] == 'user':
            raise UnauthorizedAccessError

        user_to_delete : UserModel = UserModel.query.filter_by(id=id).first()

        if not user_to_delete:
            raise InvalidUser
            
        session.delete(user_to_delete)
        session.commit()
        
    except InvalidUser as e:
        return {"error": e.message}, e.code
    
    except KeyError:
        return {"error": "Invalid token."}, HTTPStatus.UNAUTHORIZED

    except UnauthorizedAccessError as e:
        return {"error": e.message}, e.code

    return {"message": "Successfully deleted."}, HTTPStatus.OK
