from flask import Blueprint
from app.routes.leads_blueprint import bp as leads_bp

bp_api = Blueprint("bp_api", __name__, url_prefix="/api")

bp_api.register_blueprint(leads_bp)