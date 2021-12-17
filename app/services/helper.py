from app.configs.database import db
from flask import jsonify, request
from http import HTTPStatus
from app.exc import DataNotFound
from werkzeug.exceptions import NotFound
from sqlalchemy import desc


class BaseModel():
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class BaseServices():
    model = None


    @classmethod
    def get_all(cls):
        data_list = cls.model.query.order_by(desc(cls.model.id)).all()
        return jsonify(data_list), HTTPStatus.OK


    @classmethod
    def get_by_id(cls, id):
        try:
            data = cls.model.query.get_or_404(id)
            return jsonify(data), HTTPStatus.CREATED
        except NotFound:
            data_name = request.url.split('/')[-2].capitalize()
            raise DataNotFound(data_name)

    
    @classmethod
    def delete(cls, id):
        try:
            data = cls.model.query.get_or_404(id)
            data.delete()
            return {}, HTTPStatus.NO_CONTENT
        except NotFound:
            data_name = request.url.split('/')[-2].capitalize()
            raise DataNotFound(data_name)
