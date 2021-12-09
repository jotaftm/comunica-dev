from flask import request, current_app, jsonify
from http import HTTPStatus
from app.exc import InvalidCPFError, InvalidDataTypeError, InvalidEmailError
from sqlalchemy.exc import IntegrityError

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

