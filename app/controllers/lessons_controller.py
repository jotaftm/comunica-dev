from flask import request, jsonify, current_app
from app.models.lessons_model import LessonModel
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.exceptions import NotFound

from app.models.users_model import UserModel


def list_lessons():
    lessons_list = LessonModel.query.all()
    return jsonify(lessons_list)


def create_lesson():
    session = current_app.db.session

    data = request.get_json()

    new_lesson = LessonModel(**data)
        
    session.add(new_lesson)
    session.commit()

    return jsonify(new_lesson), HTTPStatus.CREATED


def update_lesson(id: int):
    data = request.get_json()

    lesson_to_update = LessonModel.query.filter_by(id=id).update(data)

    if not lesson_to_update:
        return {'error': 'Lesson does not exist'}, HTTPStatus.NOT_FOUND

    current_app.db.session.commit()

    lesson_updated = LessonModel.query.get(id)

    return jsonify(lesson_updated)


def get_lesson_by_id(id: int):
    lesson = LessonModel.query.get(id)

    if not lesson:
        return {'error': 'Lesson does not exist'}, HTTPStatus.NOT_FOUND

    return jsonify(lesson)


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

        user_found: UserModel = UserModel.query.get_or_404(user_logged['id'])

    except KeyError:
        return {"error": "Invalid token."}, HTTPStatus.UNAUTHORIZED
    
    except NotFound:
        return {"error": "User not found"}, HTTPStatus.NOT_FOUND

    return jsonify(user_found.lessons), HTTPStatus.OK