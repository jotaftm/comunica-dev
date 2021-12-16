from app.configs.database import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates, relationship, backref
from dataclasses import dataclass
from app.exc import InvalidDataTypeError, InvalidZipCodeError

from app.models.users_model import UserModel

@dataclass
class AddressModel(db.Model):
    id: int
    zip_code: str
    address: str
    number: str
    city: str
    state: str
    country: str
    user_id: int
    
    __tablename__ = 'addresses'
    
    id = Column(Integer, primary_key=True)
    zip_code = Column(String(8), nullable=False)
    address = Column(String, nullable=False)
    number = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    country = Column(String, nullable=False)
    user_id = Column(Integer, db.ForeignKey('users.id'), nullable=False)


    @validates('zip_code', 'address', 'number', 'city', 'state', 'country')
    def validate_values(self, key, value):
        if type(value) is not str:
            raise InvalidDataTypeError(key, type(value).__name__, "string")
        if key == 'zip_code' and len(value) != 8:
            raise InvalidZipCodeError(value)

        return value

    @validates('user_id')
    def validate_id(self, _, value):
        user = UserModel.query.get_or_404(value)
        return value
