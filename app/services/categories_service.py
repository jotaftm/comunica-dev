from app.exc import DataNotFound
from app.models.categories_model import CategoryModel
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus
from app.services.helper import BaseServices


class CategoryService(BaseServices):
    model = CategoryModel


    @staticmethod
    def create() -> CategoryModel:
        parser = reqparse.RequestParser()

        parser.add_argument("type", type=str, required=True)
        parser.add_argument("description", type=str, required=True)

        data = parser.parse_args(strict=True)

        new_category: CategoryModel = CategoryModel(**data)
        new_category.save()

        return jsonify(new_category), HTTPStatus.CREATED


    @staticmethod
    def update(category_id) -> CategoryModel:
        category = CategoryModel.query.get(category_id)
        if not category:
            raise DataNotFound('Category')

        parser = reqparse.RequestParser()

        parser.add_argument("type", type=str, store_missing=False)
        parser.add_argument("description", type=str, store_missing=False)

        data = parser.parse_args(strict=True)

        for key, value in data.items():
            setattr(category, key, value)
        
        category.save()
        return jsonify(category), HTTPStatus.OK
