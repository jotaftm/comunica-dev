from flask import request, jsonify, current_app
from app.models.lessons_model import LessonModel
from http import HTTPStatus
from sqlalchemy import exc


def list_lessons():
    lessons_list = LessonModel.query.all()
    return jsonify(lessons_list), 200


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