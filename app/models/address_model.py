from app.configs.database import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
from dataclasses import dataclass

from app.exc.InvalidTypeError import InvalidTypeError

@dataclass
class AddressModel(db.Model):

    id: int
    zip_code: str
    address: str
    number: str
    city: str
    state: str
    country: str
    
    __tablename__ = 'addresses'
    
    id = Column(Integer, primary_key=True)
    zip_code = Column(String(8), nullable=False)
    address = Column(String, nullable=False)
    number = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    country = Column(String, nullable=False)


    @validates('zip_code', 'address', 'number', 'city', 'state', 'country')
    def validate_values(self, _, value):
        if type(value) is not str:
            raise InvalidTypeError
        return value
