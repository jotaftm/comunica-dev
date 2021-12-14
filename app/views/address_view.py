from http import HTTPStatus
from app.exc import DataNotFound, InvalidZipCodeError, InvalidDataTypeError
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import make_response

from app.services.address_service import AddressService


class AddressResource(Resource):

    # @jwt_required()
    def get(self):
        return make_response(AddressService.get_all())


    def post(self):
        try:
            return make_response(AddressService.create())
        except InvalidDataTypeError as e:
            return {'error': str(e.message)}, HTTPStatus.BAD_REQUEST
        except InvalidZipCodeError as e:
            return {'error': str(e.message)}, HTTPStatus.BAD_REQUEST


class AddressRetrieveResource(Resource):

    # @jwt_required()
    def get(self, address_id):
        try:
            return make_response(AddressService.get_by_id(address_id))
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND
    

    # @jwt_required()
    def patch(self, address_id):
        try:
            return make_response(AddressService.update(address_id))
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND

    
    # @jwt_required()
    def delete(self, address_id):
        try:
            return make_response(AddressService.delete(address_id))
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND