from flask import Flask
from app.configs import database, migration, env_configs
from app.routes.api_blueprint import bp_api

def create_app():
    app = Flask(__name__)

    env_configs.init_app(app)

    database.init_app(app)

    migration.init_app(app)

    app.register_blueprint(bp_api)

    return app
