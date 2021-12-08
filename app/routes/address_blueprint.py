from flask import Blueprint
from app.controllers.address_controller import create_address, get_address_by_id, update_address, delete_address, get_address

bp_address = Blueprint('bp_address', __name__, url_prefix='/address')

bp_address.get('')(get_address)
bp_address.get('/<int:id>')(get_address_by_id)
bp_address.post('')(create_address)
bp_address.patch('/<int:id>')(update_address)
bp_address.delete('/<int:id>')(delete_address)
