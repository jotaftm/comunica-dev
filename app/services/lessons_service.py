from app.exc import DataNotFound
from app.models.lessons_model import LessonModel
from app.models.users_model import UserModel
from app.models.user_lesson_model import UserLessonModel
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus
from app.services.helper import BaseServices
from flask_jwt_extended import get_jwt_identity
from sqlalchemy.sql.elements import and_


class LessonService(BaseServices):
    model = LessonModel


    @staticmethod
    def create() -> LessonModel:
        parser = reqparse.RequestParser()

        parser.add_argument("title", type=str, required=True)
        parser.add_argument("description", type=str, required=True)
        parser.add_argument("url_video", type=str, required=True)
        parser.add_argument("is_premium", type=bool, required=True)
        parser.add_argument("category", type=dict, required=True)

        data = parser.parse_args(strict=True)

        new_lesson: LessonModel = LessonModel(**data)
        new_lesson.save()

        return jsonify(new_lesson), HTTPStatus.CREATED


    @staticmethod
    def update(lesson_id) -> LessonModel:
        lesson = LessonModel.query.get(lesson_id)
        if not lesson:
            raise DataNotFound('Lesson')

        parser = reqparse.RequestParser()

        parser.add_argument("title", type=str, store_missing=False)
        parser.add_argument("description", type=str, store_missing=False)
        parser.add_argument("url_video", type=str, store_missing=False)
        parser.add_argument("is_premium", type=bool, store_missing=False)
        parser.add_argument("category", type=dict, store_missing=False)

        data = parser.parse_args(strict=True)

        for key, value in data.items():
            setattr(lesson, key, value)
        
        lesson.save()
        return jsonify(lesson), HTTPStatus.OK


    @staticmethod
    def list_my_lessons():
        user_logged = get_jwt_identity()

        user_found: UserModel = UserModel.query.get(user_logged['id'])

        if not user_found:
            raise DataNotFound('User')

        return jsonify(user_found.lessons), HTTPStatus.OK


    @staticmethod
    def update_finished(id):
        user = get_jwt_identity()
        result = {"finished": True}
        user_lesson = UserLessonModel.query.filter(
                and_(UserLessonModel.lesson_id==id, UserLessonModel.user_id==user['id'])
            ).update(result) 
        
        if not user_lesson:
            return {"error": "User and lesson doesn't match!"}, HTTPStatus.NOT_FOUND

        user_lesson.save()
        
        user_lesson_updated = UserLessonModel.query.filter(
                and_(UserLessonModel.lesson_id==id, UserLessonModel.user_id==user['id'])
            ).first()

        return jsonify(user_lesson_updated), HTTPStatus.OK
