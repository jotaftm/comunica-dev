from flask import Blueprint
from app.controllers.insomnia_controller import (
    insomnia_controller
) 

bp = Blueprint('insomnia_bp', __name__, url_prefix='insomnia')

bp.get('')(insomnia_controller)