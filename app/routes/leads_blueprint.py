from flask import Blueprint
from app.controllers.leads_controller import (
    create_lead,
    list_leads,
    update_lead,
    get_lead_by_id,
    delete_lead
) 

bp = Blueprint('leads_bp', __name__, url_prefix='leads')

bp.post('')(create_lead)
bp.get('')(list_leads)
bp.get('/<int:id>')(get_lead_by_id)
bp.delete('/<int:id>')(delete_lead)
bp.patch('/<int:id>')(update_lead)