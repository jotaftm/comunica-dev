from flask import request, current_app, jsonify
from http import HTTPStatus
from app.exc.InvalidTypeError import InvalidTypeError
from werkzeug.exceptions import NotFound
from app.models.address_model import AddressModel
import sqlalchemy
import psycopg2


def create_address():
    session = current_app.db.session
    data = request.get_json()
    
    try:
        address = AddressModel(**data)

        session.add(address)
        session.commit()

        return jsonify(address), HTTPStatus.CREATED

    except InvalidTypeError:
        return {'error': f'Invalid options. All values must be strings.'}, HTTPStatus.CONFLICT
    except sqlalchemy.exc.IntegrityError as e:
        if type(e.orig) == psycopg2.errors.NotNullViolation:
            return {'error': 'All fields must be filled in!'}, HTTPStatus.CONFLICT


def update_address(id: int):
    session = current_app.db.session
    data = request.get_json()

    try:
        address = AddressModel.query.get_or_404(id)

        address = AddressModel.query.filter_by(id=id).update(data)
        session.commit()

        address = AddressModel.query.get(id)
    
    except NotFound:
        return {'error': 'Address not found!'}, HTTPStatus.NOT_FOUND

    return jsonify(address), HTTPStatus.OK


def delete_address(id: int):
    session = current_app.db.session

    try:
        address = AddressModel.query.get_or_404(id)

        session.delete(address)
        session.commit()

    except NotFound:
        return {'error': 'Address not found!'}, HTTPStatus.NOT_FOUND

    return '', HTTPStatus.NO_CONTENT


def get_address():
    address_list = AddressModel.query.all()

    return jsonify(address_list)
    
def get_address_by_id(id: int):
    try:
        address = AddressModel.query.get_or_404(id)

    except NotFound:
        return {'error': 'Address not found!'}, HTTPStatus.NOT_FOUND

    return jsonify(address), HTTPStatus.OK
