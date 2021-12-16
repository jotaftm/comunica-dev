from app.exc import DataAlreadyRegistered, DataNotFound, EmailVerifiedError, InvalidEmailError, InvalidDataTypeError, InvalidCPFError, InvalidPassword, InvalidKey, UnauthorizedAccessError
from flask_restful import Resource
from flask import make_response
from flask_jwt_extended import jwt_required

from app.services.users_service import UserService


class UserResource(Resource):

    def get(self):
        return make_response(UserService.get_all())


class UserRetrieveResource(Resource):

    @jwt_required()
    def get(self, user_id):
        try:
            return make_response(UserService.get_by_id(user_id))
        except DataNotFound as e:
            return e.message, e.code
        except UnauthorizedAccessError as e:
            return e.message, e.code
    

    @jwt_required()
    def patch(self, user_id):
        try:
            return make_response(UserService.update(user_id))
        except DataNotFound as e:
            return e.message, e.code
        except UnauthorizedAccessError as e:
            return e.message, e.code
        except InvalidPassword as e:
            return e.message, e.code

    
    @jwt_required()
    def delete(self, user_id):
        try:
            return make_response(UserService.delete(user_id))
        except DataNotFound as e:
            return e.message, e.code
        except UnauthorizedAccessError as e:
            return e.message, e.code


class UserBasicResource(Resource):

    @jwt_required()
    def post(self):
        try:
            return make_response(UserService.create())
        except InvalidEmailError as e:
            return e.message, e.code
        except DataAlreadyRegistered as e:
            return e.message, e.code
        except InvalidDataTypeError as e:
            return e.message, e.code
        except InvalidCPFError as e:
            return e.message, e.code
        except InvalidKey as e:
            return e.message, e.code


class UserValidateTokenResource(Resource):

    def get(self, token):
        try:
            return make_response(UserService.verify_user(token))
        except EmailVerifiedError as e:
            return e.message, e.code


class UserLoginResource(Resource):

    def post(self):
        try:
            return make_response(UserService.user_login())
        except DataNotFound as e:
            return e.message, e.code
        except InvalidPassword as e:
            return e.message, e.code


class UserConfirmPasswordResetResource(Resource):

    def post(self):
        try:
            return make_response(UserService.confirm_password_reset())
        except DataNotFound as e:
            return e.message, e.code


class UserPasswordResetResource(Resource):

    def post(self):
        try:
            return make_response(UserService.reset_user_password())
        except DataNotFound as e:
            return e.message, e.code
