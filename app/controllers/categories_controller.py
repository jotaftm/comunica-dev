from flask import request, jsonify, current_app
from app.configs.decorators import verify_role_admin
from app.models.categories_model import CategoryModel
from http import HTTPStatus
from flask_jwt_extended import jwt_required


@jwt_required()
@verify_role_admin
def list_categories():
    categories_list = CategoryModel.query.all()

    return jsonify(categories_list), HTTPStatus.OK


@jwt_required()
@verify_role_admin
def create_category():
    session = current_app.db.session

    data = request.get_json()

    new_category = CategoryModel(**data)
        
    session.add(new_category)
    session.commit()
    
    return jsonify(new_category), HTTPStatus.CREATED


@jwt_required()
@verify_role_admin
def update_category(id: int):
    data = request.get_json()

    category_to_update = CategoryModel.query.filter_by(id=id).update(data)

    if not category_to_update:
        return {'error': 'Category does not exist'}, HTTPStatus.NOT_FOUND

    current_app.db.session.commit()

    category_updated = CategoryModel.query.get(id)

    return jsonify(category_updated), HTTPStatus.OK


@jwt_required()
@verify_role_admin
def get_category_by_id(id: int):
    category = CategoryModel.query.get(id)

    if not category:
        return {'error': 'Category does not exist'}, HTTPStatus.NOT_FOUND

    return jsonify(category), HTTPStatus.OK


@jwt_required()
@verify_role_admin
def delete_category(id: int):
    category = CategoryModel.query.get(id)

    if not category:
        return {'error': 'Category does not exist'}, HTTPStatus.NOT_FOUND
    
    current_app.db.session.delete(category)

    current_app.db.session.commit()

    return "", HTTPStatus.NO_CONTENT