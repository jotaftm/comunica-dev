from flask import request, jsonify, current_app
from sqlalchemy.sql.elements import and_
from app.configs.decorators import verify_role_admin
from app.exc import UnauthorizedAccessError
from app.models.lessons_model import LessonModel
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.exceptions import NotFound
from app.models.user_lesson_model import UserLessonModel


@jwt_required()
@verify_role_admin
def list_lessons():
    lessons_list = LessonModel.query.all()

    return jsonify(lessons_list), HTTPStatus.OK


@jwt_required()
@verify_role_admin
def create_lesson():
    session = current_app.db.session

    data = request.get_json()

    new_lesson = LessonModel(**data)
        
    session.add(new_lesson)
    session.commit()

    return jsonify(new_lesson), HTTPStatus.CREATED


@jwt_required()
@verify_role_admin
def update_lesson(id: int):
    data = request.get_json()

    lesson_to_update = LessonModel.query.filter_by(id=id).update(data)

    if not lesson_to_update:
        return {'error': 'Lesson does not exist'}, HTTPStatus.NOT_FOUND

    current_app.db.session.commit()

    lesson_updated = LessonModel.query.get(id)

    return jsonify(lesson_updated), HTTPStatus.OK


@jwt_required()
def get_lesson_by_id(id: int):
    try:
        user_logged = get_jwt_identity()

        lesson: LessonModel = LessonModel.query.get(id)

        if not user_logged['is_premium'] and lesson.is_premium:
            raise UnauthorizedAccessError

        if not lesson:
            return {'error': 'Lesson does not exist'}, HTTPStatus.NOT_FOUND
    
    except UnauthorizedAccessError as e:
        return {"error": e.message}, e.code

    return jsonify(lesson), HTTPStatus.OK


@jwt_required()
@verify_role_admin
def delete_lesson(id: int):
    lesson = LessonModel.query.get(id)

    if not lesson:
        return {'error': 'Lesson does not exist'}, HTTPStatus.NOT_FOUND
    
    current_app.db.session.delete(lesson)

    current_app.db.session.commit()

    return "", HTTPStatus.NO_CONTENT


@jwt_required()
def list_my_lessons():
    try:
        user_logged = get_jwt_identity()

        user_lesson: UserLessonModel = UserLessonModel.query.filter_by(user_id=user_logged['id']).all()

    except KeyError:
        return {"error": "Invalid token."}, HTTPStatus.UNAUTHORIZED
    
    except NotFound:
        return {"error": "User not found"}, HTTPStatus.NOT_FOUND

    return jsonify(user_lesson), HTTPStatus.OK


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