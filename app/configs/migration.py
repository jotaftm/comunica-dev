from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask):
   from app.models.leads_model import LeadModel
   from app.models.users_model import UserModel
   from app.models.categories_model import CategoryModel
   from app.models.lessons_model import LessonModel
   from app.models.user_token_model import UserTokenModel

   Migrate(app, app.db)
