from flask import request, current_app, jsonify
from http import HTTPStatus
from app.exc import InvalidCPFError, InvalidDataTypeError, InvalidEmailError, InvalidPassword, InvalidUser, InvalidKey
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.exceptions import NotFound

from app.models.users_model import UserModel


def create_basic_user():
    try:
        session = current_app.db.session

        data = request.get_json()

        new_user = UserModel(**data)

        session.add(new_user)
        session.commit()

    # todo enviar email de confirmação passando token

    except InvalidDataTypeError as e:
        return {"error": e.message}, e.code

    except InvalidEmailError as e:
        return {"error": e.message}, e.code

    except InvalidCPFError as e:
        return {"error": e.message}, e.code

    except IntegrityError:
        return {"error": "User already exists."}, HTTPStatus.CONFLICT

    return jsonify(new_user), HTTPStatus.CREATED


# todo verificar token
def verify_user():
    ...


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
def get_one_user(id):
    try:
        user_token = get_jwt_identity()

        if user_token['id'] != id:
            raise InvalidUserIdAccess

        found_user: UserModel = UserModel.query.filter_by(
            id=user_token['id']).first_or_404()

        return jsonify(found_user)

    except NotFound:
        return {"error": "User not found"}, HTTPStatus.NOT_FOUND

    except InvalidUserIdAccess as e:
        return {"error": e.message}, e.code


@jwt_required()
def update_user():
    try:
        session = current_app.db.session

        user_token = get_jwt_identity()
        data = request.get_json()
        data_keys = data.keys()
        valid_keys = ["email",
                      "name",
                      "cpf"]
        updated_user: UserModel = UserModel.query.filter_by(id=user_token['id']).first()

        if not updated_user:
            raise InvalidUser
            
        for key in data_keys:
            if key not in valid_keys:
                raise InvalidKey(key)
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

    except IntegrityError:
        return {"error": "User already exists."}, HTTPStatus.CONFLICT
    
    return jsonify(found_user), HTTPStatus.ACCEPTED
