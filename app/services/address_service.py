from app.exc import DataNotFound
from app.models.address_model import AddressModel
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus
from app.services.helper import BaseServices


class AddressService(BaseServices):
    model = AddressModel


    @staticmethod
    def create() -> AddressModel:
        parser = reqparse.RequestParser()

        parser.add_argument("zip_code", type=str, required=True)
        parser.add_argument("address", type=str, required=True)
        parser.add_argument("number", type=str, required=True)
        parser.add_argument("city", type=str, required=True)
        parser.add_argument("state", type=str, required=True)
        parser.add_argument("country", type=str, required=True)
        parser.add_argument("user_id", type=int, required=True)

        data = parser.parse_args(strict=True)

        new_address: AddressModel = AddressModel(**data)
        new_address.save()

        return jsonify(new_address), HTTPStatus.CREATED


    @staticmethod
    def update(address_id) -> AddressModel:
        address = AddressModel.query.get(address_id)
        if not address:
            raise DataNotFound('Address')

        parser = reqparse.RequestParser()

        parser.add_argument("zip_code", type=str, store_missing=False)
        parser.add_argument("address", type=str, store_missing=False)
        parser.add_argument("number", type=str, store_missing=False)
        parser.add_argument("city", type=str, store_missing=False)
        parser.add_argument("state", type=str, store_missing=False)
        parser.add_argument("country", type=str, store_missing=False)

        data = parser.parse_args(strict=True)

        for key, value in data.items():
            setattr(address, key, value)
        
        address.save()
        return jsonify(address), HTTPStatus.OK