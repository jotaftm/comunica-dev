from flask import request, current_app, jsonify
from http import HTTPStatus
from app.configs.decorators import verify_role_admin
from app.exc import InvalidDataTypeError, InvalidZipCodeError, UnauthorizedAccessError
from app.models.address_model import AddressModel
from werkzeug.exceptions import NotFound
import sqlalchemy
import psycopg2
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.users_model import UserModel


@jwt_required()
def create_address():
    session = current_app.db.session
    data = request.get_json()
    
    try:
        user_logged = get_jwt_identity()

        data['user_id'] = user_logged['id']

        address = AddressModel(**data)

        session.add(address)
        session.commit()

        return jsonify(address), HTTPStatus.CREATED

    except sqlalchemy.exc.IntegrityError as e:
        if type(e.orig) == psycopg2.errors.NotNullViolation:
            return {'error': 'All fields must be filled in!'}, HTTPStatus.CONFLICT

    except InvalidDataTypeError as e:
        return {'error': str(e.message)}, e.code

    except InvalidZipCodeError as e:
        return {'error': str(e.message)}, e.code

    except NotFound:
        return {'error': 'Inexistent User ID.'}, HTTPStatus.BAD_REQUEST

    except KeyError:
        return {"error": "Invalid token."}, HTTPStatus.UNAUTHORIZED


@jwt_required()
def update_address(id: int):
    session = current_app.db.session
    data = request.get_json()

    try:
        user_logged = get_jwt_identity()

        address: AddressModel = AddressModel.query.get_or_404(id)

        if address.user_id != user_logged['id'] and user_logged['user_role'] == 'user':
            raise UnauthorizedAccessError

        address = AddressModel.query.filter_by(id=id).update(data)
        session.commit()

        address = AddressModel.query.get(id)
    
    except NotFound:
        return {'error': 'Address not found!'}, HTTPStatus.NOT_FOUND

    except KeyError:
        return {"error": "Invalid token."}, HTTPStatus.UNAUTHORIZED

    except UnauthorizedAccessError as e:
        return {"error": e.message}, e.code

    return jsonify(address), HTTPStatus.OK


@jwt_required()
def delete_address(id: int):
    session = current_app.db.session

    try:
        user_logged = get_jwt_identity()

        address: AddressModel = AddressModel.query.get_or_404(id)

        if address.user_id != user_logged['id'] and user_logged['user_role'] == 'user':
            raise UnauthorizedAccessError

        session.delete(address)
        session.commit()

    except NotFound:
        return {'error': 'Address not found!'}, HTTPStatus.NOT_FOUND

    except KeyError:
        return {"error": "Invalid token."}, HTTPStatus.UNAUTHORIZED

    except UnauthorizedAccessError as e:
        return {"error": e.message}, e.code

    return '', HTTPStatus.NO_CONTENT


@jwt_required()
@verify_role_admin
def get_address():
    address_list = AddressModel.query.all()

    return jsonify(address_list)


@jwt_required()
def get_my_addresses():
    try:
        user_logged = get_jwt_identity()
        
        user_found: UserModel = UserModel.query.get_or_404(user_logged['id'])

    except KeyError:
        return {"error": "Invalid token."}, HTTPStatus.UNAUTHORIZED
    
    except NotFound:
        return {"error": "User not found"}, HTTPStatus.NOT_FOUND

    return jsonify(user_found.addresses), HTTPStatus.OK


@jwt_required()
def get_address_by_id(id: int):
    try:
        user_logged = get_jwt_identity()

        address: AddressModel = AddressModel.query.get_or_404(id)

        if address.user_id != user_logged['id'] and user_logged['user_role'] == 'user':
            raise UnauthorizedAccessError

    except NotFound:
        return {'error': 'Address not found!'}, HTTPStatus.NOT_FOUND
    
    except KeyError:
        return {"error": "Invalid token."}, HTTPStatus.UNAUTHORIZED

    except UnauthorizedAccessError as e:
        return {"error": e.message}, e.code

    return jsonify(address), HTTPStatus.OK
