from flask import request, jsonify, current_app
from app.models.user_lesson_model import UserLessonModel
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity


@jwt_required()
def update_finished(lesson_id):
    user = get_jwt_identity()
    result = {"finished": True}
    user_lesson = UserLessonModel.query.filter(lesson_id=lesson_id, user_id=user['id']).update(result) 
    
    if not user_lesson:
        return {"error": "User and lesson doesn't match!"}, HTTPStatus.NOT_FOUND

    current_app.db.session.commit()
    user_lesson_updated = UserLessonModel.query.get(lesson_id, user['id'])

    return jsonify(user_lesson_updated)

