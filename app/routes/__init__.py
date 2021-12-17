from app.routes.api_blueprint import bp_api
from flask import Flask

def init_app(app: Flask):
   app.register_blueprint(bp_api)