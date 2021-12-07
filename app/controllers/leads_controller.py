from flask import request, jsonify, current_app
from app.models.leads_model import LeadModel
from app.exc.leads_exc import InvalidEmailFormat
from http import HTTPStatus
from sqlalchemy import exc


def list_leads():
    leads_list = LeadModel.query.all()
    return jsonify(leads_list), 200


def create_lead():
    try:
        session = current_app.db.session

        data = request.get_json()

        for key, value in data.items():
            if key not in ['name', 'email'] or not len(data) == 2 or not type(value) == str:
                return {'error': 'O corpo da requisição deve conter obrigatoriamente os campos name e email e ambos devem ser do tipo string'}

        normalized_data = {
            "name": data['name'].title(),
            "email": data['email'].lower()
        }
        new_lead = LeadModel(**normalized_data)
            
        session.add(new_lead)
        session.commit()

        return jsonify(new_lead), HTTPStatus.CREATED
    except InvalidEmailFormat as e:
        return {'error': str(e)}, HTTPStatus.BAD_REQUEST
    except exc.IntegrityError:
        return jsonify({'msg': 'Lead already exists'}), HTTPStatus.CONFLICT


def update_lead(id: int):
    data = request.get_json()

    lead_to_update = LeadModel.query.filter_by(id=id).update(data)

    if not lead_to_update:
        return {'error': 'lead not found'}, HTTPStatus.NOT_FOUND

    current_app.db.session.commit()

    lead_updated = LeadModel.query.get(id)

    return jsonify(lead_updated)


def get_lead_by_id(id: int):
    lead = LeadModel.query.get(id)

    if not lead:
        return {'error': 'lead not found'}, HTTPStatus.NOT_FOUND

    return jsonify(lead)


def delete_lead(id: int):
    lead = LeadModel.query.get(id)

    if not lead:
        return {'error': 'lead not found'}, HTTPStatus.NOT_FOUND
    
    current_app.db.session.delete(lead)
    current_app.db.session.commit()
    return "", HTTPStatus.NO_CONTENT