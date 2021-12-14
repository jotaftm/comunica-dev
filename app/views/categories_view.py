from http import HTTPStatus
from app.exc import DataNotFound, InvalidZipCodeError, InvalidDataTypeError
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import make_response

from app.services.categories_service import CategoryService


class CategoryResource(Resource):

    # @jwt_required()
    def get(self):
        return make_response(CategoryService.get_all())


    def post(self):
        return make_response(CategoryService.create())


class CategoryRetrieveResource(Resource):

    # @jwt_required()
    def get(self, category_id):
        try:
            return make_response(CategoryService.get_by_id(category_id))
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND
    

    # @jwt_required()
    def patch(self, category_id):
        try:
            return make_response(CategoryService.update(category_id))
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND

    
    # @jwt_required()
    def delete(self, category_id):
        try:
            return make_response(CategoryService.delete(category_id))
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND