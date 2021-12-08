from flask import request, current_app, jsonify
from http import HTTPStatus
from app.exc.InvalidTypeError import InvalidTypeError
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


def update_address(id: int):
    session = current_app.db.session
    data = request.get_json()

    address = AddressModel.query.get(id)
    if not address:
        return {'msg': 'Address not found!'}, HTTPStatus.NOT_FOUND

    address = AddressModel.query.filter_by(id=id).update(data)
    session.commit()

    address = AddressModel.query.get(id)

    return jsonify(address), HTTPStatus.OK


def delete_address(id: int):
    session = current_app.db.session

    address = AddressModel.query.get(id)

    if not address:
        return {'error': 'Address not found!'}, HTTPStatus.NOT_FOUND

    session.delete(address)
    session.commit()

    return '', HTTPStatus.NO_CONTENT


def get_address():
    address_list = AddressModel.query.all()

    return jsonify(address_list)
    
def get_address_by_id(id: int):
    address = AddressModel.query.get(id)

    if not address:
        return {'error': 'Address not found!'}, HTTPStatus.NOT_FOUND

    return jsonify(address), HTTPStatus.OK
