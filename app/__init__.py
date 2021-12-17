from click.decorators import command
from flask import Flask
from app.configs import commands, database, migration, env_configs, auth_jwt, api


def create_app():
    app = Flask(__name__)

    env_configs.init_app(app)
    database.init_app(app)
    migration.init_app(app)
    commands.init_app(app)
    auth_jwt.init_app(app)
    api.init_app(app)

    return app
