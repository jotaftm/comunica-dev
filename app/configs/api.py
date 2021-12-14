from flask import Flask
from flask_restful import Api


def init_app(app: Flask) -> None:
    api = Api(app)

    from app.models.leads_model import LeadModel
    from app.models.users_model import UserModel
    from app.models.categories_model import CategoryModel
    from app.models.lessons_model import LessonModel
    from app.models.user_token_model import UserTokenModel
    from app.models.user_lesson_model import UserLessonModel
    from app.models.captchas_model import CaptchaModel

    from app.views.address_view import AddressResource, AddressRetrieveResource
    api.add_resource(AddressResource, "/api/address", endpoint="ADDRESSES")
    api.add_resource(AddressRetrieveResource, "/api/address/<int:address_id>", endpoint="ADDRESS_ID")
