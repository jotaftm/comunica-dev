from http import HTTPStatus
from app.exc import DataNotFound, InvalidEmailError, LeadExistsError
from sqlalchemy.exc import IntegrityError
from flask_restful import Resource
from flask import make_response, jsonify

from app.services.leads_service import LeadService


class LeadResource(Resource):

    def get(self):
        return make_response(LeadService.get_all())


    def post(self):
        try:
            return make_response(LeadService.create())
        except InvalidEmailError as e:
            return {'error': e.message}, HTTPStatus.BAD_REQUEST
        except LeadExistsError as e:
            return {'error': e.message}, HTTPStatus.CONFLICT


class LeadRetrieveResource(Resource):

    def get(self, lead_id):
        try:
            return make_response(LeadService.get_by_id(lead_id))
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND
    

    def patch(self, lead_id):
        try:
            return make_response(LeadService.update(lead_id))
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND

    
    def delete(self, lead_id):
        try:
            return make_response(LeadService.delete(lead_id))
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND


class LeadSendEmailResource(Resource):
    def send(self):
        return make_response(LeadService.newsletter_info())
