from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask):
   from app.models.leads_model import LeadModel
   from app.models.users_model import UserModel

   Migrate(app, app.db)
