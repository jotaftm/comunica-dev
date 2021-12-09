from flask import Blueprint
from app.routes.address_blueprint import bp_address
from app.routes.leads_blueprint import bp as leads_bp
from app.routes.categories_blueprint import bp as categories_bp
from app.routes.lessons_blueprint import bp as lessons_bp


bp_api = Blueprint("bp_api", __name__, url_prefix="/api")
bp_api.register_blueprint(bp_address)
bp_api.register_blueprint(leads_bp)
bp_api.register_blueprint(categories_bp)
bp_api.register_blueprint(lessons_bp)
