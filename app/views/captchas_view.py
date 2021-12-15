from app.exc import DataNotFound
from flask_restful import Resource
from flask import make_response

from app.services.captchas_service import CaptchaService


class CaptchaGenerateResource(Resource):


    def post(self, num_chars):
        return make_response(CaptchaService.generate_captcha(num_chars))


class CaptchaValidateResource(Resource):
    

    def post(self):
        try:
            return make_response(CaptchaService.validate_captcha())
        except DataNotFound as e:
            return e.message, e.code
