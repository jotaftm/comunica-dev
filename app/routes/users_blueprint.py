from flask import Blueprint

from app.controllers.users_controller import (
    create_basic_user, 
    user_login, 
    get_my_data, 
    verify_user, 
    update_user,
    confirm_password_reset,
    reset_user_password,
    delete_user,
    list_users,
    get_one_user
)

bp_users = Blueprint("bp_users", __name__, url_prefix="/users")

bp_users.post('/basic')(create_basic_user)
bp_users.post('/login')(user_login)
bp_users.patch('/<int:id>')(update_user)
bp_users.get('/personal')(get_my_data)
bp_users.get('')(list_users)
bp_users.get('/<int:id>')(get_one_user)
bp_users.get('/validate/<token>')(verify_user)
bp_users.post('/confirm/email')(confirm_password_reset)
bp_users.post('/reset/password')(reset_user_password)
bp_users.delete('/<int:id>')(delete_user)
