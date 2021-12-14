from flask import Blueprint

from app.controllers.user_lesson_controller import update_finished

bp_user_lesson = Blueprint("bp_user_lesson", __name__, url_prefix="/users-lessons")

bp_user_lesson.patch('/<int:id>')(update_finished)
