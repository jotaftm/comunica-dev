from flask import request, jsonify, current_app
from app.models.leads_model import LeadModel
from app.exc import InvalidEmailError
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError


def list_leads():
    leads_list = LeadModel.query.all()
    return jsonify(leads_list)


def create_lead():
    try:
        session = current_app.db.session

        data = request.get_json()

        for key, value in data.items():
            if key not in ['name', 'email'] or not len(data) == 2 or not type(value) == str:
                return {'error': 'Request body must contain only email and name fields, and both must be of type string'}, HTTPStatus.BAD_REQUEST

        normalized_data = {
            "name": data['name'].title(),
            "email": data['email'].lower()
        }
        new_lead = LeadModel(**normalized_data)
            
        session.add(new_lead)
        session.commit()

        return jsonify(new_lead), HTTPStatus.CREATED

    except InvalidEmailError as e:
        return {'error': e.message}, e.code

    except IntegrityError:
        return jsonify({'error': 'Lead already exists'}), HTTPStatus.CONFLICT


def update_lead(id: int):
    data = request.get_json()

    lead_to_update = LeadModel.query.filter_by(id=id).update(data)

    if not lead_to_update:
        return {'error': 'Lead does not exist'}, HTTPStatus.NOT_FOUND

    current_app.db.session.commit()

    lead_updated = LeadModel.query.get(id)

    return jsonify(lead_updated)


def get_lead_by_id(id: int):
    lead = LeadModel.query.get(id)

    if not lead:
        return {'error': 'Lead does not exist'}, HTTPStatus.NOT_FOUND

    return jsonify(lead)


def delete_lead(id: int):
    lead = LeadModel.query.get(id)

    if not lead:
        return {'error': 'Lead does not exist'}, HTTPStatus.NOT_FOUND
    
    current_app.db.session.delete(lead)

    current_app.db.session.commit()

    return "", HTTPStatus.NO_CONTENT