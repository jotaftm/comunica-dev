from flask import Blueprint

from app.controllers.users_controller import create_basic_user, user_login, get_one_user

bp_users = Blueprint("bp_users", __name__, url_prefix="/users")

bp_users.post('/basic')(create_basic_user)
bp_users.post('/login')(user_login)
bp_users.post('/<int:id>')(get_one_user)

