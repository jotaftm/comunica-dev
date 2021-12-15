from flask_jwt_extended import get_jwt_identity
from app.models.users_model import UserModel
from functools import wraps
from http import HTTPStatus


def verify_role_admin(func):
    @wraps(func)
    def security_func(*args, **kwargs):
        jwt_data = get_jwt_identity()

        user: UserModel = UserModel.query.filter_by(id=jwt_data['id']).first()

        if user.user_role != 'admin':
            return {"error": "Exclusive resource for admin."}, HTTPStatus.UNAUTHORIZED
        else:
            return func(*args, **kwargs)

    return security_func