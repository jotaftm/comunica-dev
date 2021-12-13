from os import access
from flask import request, current_app, jsonify
from http import HTTPStatus
from app.exc import InvalidCPFError, InvalidDataTypeError, InvalidEmailError, InvalidPassword
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token
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

        found_user: UserModel = UserModel.query.filter_by(email=email).first_or_404()

        if found_user.check_password(password):
            access_token = create_access_token(identity=found_user)
            return {"token": access_token}, HTTPStatus.OK

    except NotFound:
        return {"error": "User not found"}, HTTPStatus.NOT_FOUND

    except InvalidPassword as e:
        return {"error": e.message}, e.code
