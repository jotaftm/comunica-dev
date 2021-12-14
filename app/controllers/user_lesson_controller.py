from flask import jsonify, current_app
from sqlalchemy.sql.elements import and_
from app.models.user_lesson_model import UserLessonModel
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity


@jwt_required()
def update_finished(id):
    user = get_jwt_identity()
    result = {"finished": True}
    user_lesson = UserLessonModel.query.filter(
            and_(UserLessonModel.lesson_id==id, UserLessonModel.user_id==user['id'])
        ).update(result) 
    
    if not user_lesson:
        return {"error": "User and lesson doesn't match!"}, HTTPStatus.NOT_FOUND

    current_app.db.session.commit()
    user_lesson_updated = UserLessonModel.query.filter(
            and_(UserLessonModel.lesson_id==id, UserLessonModel.user_id==user['id'])
        ).first()

    return jsonify(user_lesson_updated), HTTPStatus.OK
