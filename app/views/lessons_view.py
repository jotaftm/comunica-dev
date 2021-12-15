from http import HTTPStatus
from app.exc import DataNotFound
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import make_response

from app.services.lessons_service import LessonService


class LessonResource(Resource):

    def get(self):
        return make_response(LessonService.get_all())


    def post(self):
        return make_response(LessonService.create())


class LessonRetrieveResource(Resource):

    def get(self, lesson_id):
        try:
            return make_response(LessonService.get_by_id(lesson_id))
        except DataNotFound as e:
            return e.message, e.code
    

    def patch(self, lesson_id):
        try:
            return make_response(LessonService.update(lesson_id))
        except DataNotFound as e:
            return e.message, e.code

    
    def delete(self, lesson_id):
        try:
            return make_response(LessonService.delete(lesson_id))
        except DataNotFound as e:
            return e.message, e.code


class LessonListByUserResource(Resource):

    @jwt_required()
    def get(self):
        try:
            return make_response(LessonService.list_my_lessons())
        except KeyError:
            return {'error': 'Invalid token.'}, HTTPStatus.UNAUTHORIZED


class LessonUpdateFinishedResource(Resource):

    @jwt_required()
    def get(self, id):
        return make_response(LessonService.update_finished(id))
