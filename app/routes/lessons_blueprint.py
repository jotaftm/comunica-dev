from flask import Blueprint
from app.controllers.lessons_controller import (
    create_lesson,
    list_lessons,
    update_lesson,
    get_lesson_by_id,
    delete_lesson
) 
from app.controllers.user_lesson_controller import update_finished

bp = Blueprint('lessons_bp', __name__, url_prefix='lessons')

bp.post('')(create_lesson)
bp.get('')(list_lessons)
bp.get('/<int:id>')(get_lesson_by_id)
bp.delete('/<int:id>')(delete_lesson)
bp.patch('/<int:id>')(update_lesson)
bp.patch('/finished/<int:id>')(update_finished)