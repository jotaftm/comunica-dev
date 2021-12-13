from os import access
from flask import request, current_app, jsonify
from http import HTTPStatus
from app.exc import (
    InvalidCPFError, 
    InvalidDataTypeError, 
    InvalidEmailError, 
    InvalidPassword, 
    EmailVerifiedError
)
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token
from werkzeug.exceptions import NotFound
from datetime import datetime, timedelta

from app.services.verify_user_email import verify_user_email

from app.models.users_model import UserModel
from app.models.user_token_model import UserTokenModel


def create_basic_user():
    try:
        session = current_app.db.session

        data = request.get_json()

        new_user = UserModel(**data)
        
        session.add(new_user)
        session.commit()

        access_token = create_access_token(new_user, expires_delta=timedelta(minutes=5))

        found_user = UserModel.query.filter_by(email=new_user.email).first()

        if found_user:
            info_token = {
                "user_id": found_user.id,
                "token": access_token,
                "token_expire": datetime.today()
            }
        else:
            return {'error': 'Failed to find user on database'}, 401

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

        return jsonify(user_updated), 200
    
    except EmailVerifiedError as e:
        return {"error": e.message}, e.code


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
