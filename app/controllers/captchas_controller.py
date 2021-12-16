from flask import request, current_app, jsonify
from http import HTTPStatus
from flask_jwt_extended import create_access_token

from app.services.generate_image_captcha import generate_image_captcha
from app.models.captchas_model import CaptchaModel

from werkzeug.exceptions import NotFound



def generate_captcha():
    session = current_app.db.session

    captcha_content, url_captcha = generate_image_captcha(6)

    new_captcha = CaptchaModel(captcha_content=captcha_content, url_captcha=url_captcha)

    session.add(new_captcha)
    session.commit()
        
    return jsonify(new_captcha), HTTPStatus.CREATED


def validate_captcha():
    try:
        data = request.get_json()

        url_captcha = data["url_captcha"]
        input_user = data["input_user"]

        found_captcha: CaptchaModel = CaptchaModel.query.filter_by(url_captcha=url_captcha).first_or_404()

        if input_user == found_captcha.captcha_content:
            access_token = create_access_token(found_captcha)

            current_app.db.session.delete(found_captcha)
            current_app.db.session.commit()

            return jsonify({"access_token": access_token}), HTTPStatus.OK

    except NotFound:
        return jsonify({"error": "Captcha not found."}), HTTPStatus.NOT_FOUND

    return jsonify({"error": "Not authorized."}), HTTPStatus.BAD_REQUEST
