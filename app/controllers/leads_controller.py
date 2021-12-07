from flask import request, jsonify, current_app
from app.models.leads_model import LeadModel


def list_leads():
    leads_list = LeadModel.query.all()
    return jsonify(leads_list), 200


def create_lead():
    session = current_app.db.session

    data = request.get_json()

    new_lead = LeadModel(**data)
        
    session.add(new_lead)
    session.commit()

    return jsonify(new_lead), 201


def update_lead(id: int):
    data = request.get_json()

    lead_to_update = LeadModel.query.filter_by(id=id).update(data)

    if not lead_to_update:
        return {'error': 'lead not found'}, 404

    current_app.db.session.commit()

    lead_updated = LeadModel.query.get(id)

    return jsonify(lead_updated)


def get_lead_by_id(id: int):
    lead = LeadModel.query.get(id)

    if not lead:
        return {'error': 'lead not found'}, 404

    return jsonify(lead)


def delete_lead(id: int):
    lead = LeadModel.query.get(id)

    if not lead:
        return {'error': 'lead not found'}, 404
    
    current_app.db.session.delete(lead)
    current_app.db.session.commit()
    return "", 204