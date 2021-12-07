from dataclasses import dataclass
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash

from app.configs.database import db


@dataclass
class UserModel(db.Model):
    email: str
    name: str
    cpf: str
    created_at: datetime
    premium_at: datetime
    premium_expire: datetime
    type_user: str
    # address: dict

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False, unique=True)
    name = Column(String(100), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    password_hash = Column(String(511), nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    premium_at = Column(DateTime)
    premium_expire = Column(DateTime)
    type_user = Column(String, nullable=False)

    # adress_id = Column(
    #   db.Integer, 
    #   db.ForeignKey('addresses.id')
    # )

    # address = db.relationship(
    #   "AddressModel",
    #   backref=db.backref("address", uselist=False)
    # )


    @property
    def password(self):
        raise AttributeError('Password is not acessible!')

    
    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    
    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)
