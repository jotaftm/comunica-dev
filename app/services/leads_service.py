from app.exc import DataNotFound, LeadExistsError
from app.models.leads_model import LeadModel
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus
from app.services.helper import BaseServices
from app.services.send_leads_newsletter import send_newsletter


class LeadService(BaseServices):
    model = LeadModel


    @staticmethod
    def create() -> LeadModel:
        parser = reqparse.RequestParser()

        parser.add_argument("email", type=str, required=True)
        parser.add_argument("name", type=str, required=True)

        data = parser.parse_args(strict=True)

        normalized_data = {
            "name": data['name'].title(),
            "email": data['email'].lower()
        }

        lead = LeadModel.query.filter_by(email=normalized_data['email']).first()

        if not lead:
            new_lead: LeadModel = LeadModel(**normalized_data)
            new_lead.save()

            return jsonify(new_lead), HTTPStatus.CREATED

        else:
            raise LeadExistsError


    @staticmethod
    def update(lead_id) -> LeadModel:
        lead = LeadModel.query.get(lead_id)
        if not lead:
            raise DataNotFound('Lead')

        parser = reqparse.RequestParser()

        parser.add_argument("email", type=str, store_missing=False)
        parser.add_argument("name", type=str, store_missing=False)

        data = parser.parse_args(strict=True)

        for key, value in data.items():
            setattr(lead, key, value)
        
        lead.save()
        return jsonify(lead), HTTPStatus.OK


    @staticmethod
    def newsletter_info() -> LeadModel:
        try:
            leads_list = LeadModel.query.all()

            parser = reqparse.RequestParser()

            parser.add_argument("subject", type=str, required=True)
            parser.add_argument("message", type=str, required=True)

            data = parser.parse_args(strict=True)

            subject = data['subject']
            message = data['message']
            recipients_emails = [lead.email for lead in leads_list]
            recipients_names =  [lead.name for lead in leads_list]

            send_newsletter(subject, message, recipients_emails, recipients_names)
            
            return {'msg': 'Emails sent successfully'}, HTTPStatus.OK
            
        except Exception:
            return {'error': 'Failed to send emails to recipients'}, HTTPStatus.UNAUTHORIZED
