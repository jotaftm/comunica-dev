from flask import Blueprint
from app.routes.leads_blueprint import bp as leads_bp
from app.routes.categories_blueprint import bp as categories_bp
from app.routes.lessons_blueprint import bp as lessons_bp
from app.routes.users_blueprint import bp_users
from app.routes.captchas_blueprint import bp_captchas
from app.controllers.insomnia_controller import insomnia_controller

bp_api = Blueprint("bp_api", __name__, url_prefix="/api")

bp_api.get("")(insomnia_controller)
bp_api.register_blueprint(leads_bp)
bp_api.register_blueprint(categories_bp)
bp_api.register_blueprint(lessons_bp)
bp_api.register_blueprint(bp_users)
bp_api.register_blueprint(bp_captchas)
