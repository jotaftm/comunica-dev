import re
from datetime import datetime
from dataclasses import dataclass
from sqlalchemy.orm import validates, relationship
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
    Boolean
)

from app.configs.database import db
from app.exc import InvalidCPFError, InvalidEmailError, InvalidDataTypeError, InvalidPassword
from app.services.helper import BaseModel


@dataclass
class UserModel(db.Model, BaseModel):
    id: int
    email: str
    name: str
    cpf: str
    created_at: datetime
    premium_at: datetime
    premium_expire: datetime
    is_premium: bool
    verified: bool

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False, unique=True)
    name = Column(String(100), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    password_hash = Column(String(511), nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    premium_at = Column(DateTime)
    premium_expire = Column(DateTime)
    is_premium = Column(Boolean, nullable=False, default=False)
    verified = Column(Boolean, nullable=False, default=False)

    token = relationship('UserTokenModel', cascade='all, delete-orphan', uselist=False)
    
    lessons = relationship('LessonModel', secondary="user_lesson")


    @validates('email', 'name', 'cpf')
    def validate_values(self, key, value):
        email_pattern = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

        if type(value) is not str:
            raise InvalidDataTypeError(key, type(value).__name__, "string")

        if key == 'email':
            if not re.fullmatch(email_pattern, value):
                raise InvalidEmailError

        if key == 'cpf':
            if not value.isnumeric() or len(value) != 11:
                raise InvalidCPFError
                
        return value


    @property
    def password(self):
        raise AttributeError('Password is not acessible!')


    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)


    def check_password(self, password_to_compare):
        if not check_password_hash(self.password_hash, password_to_compare):
            raise InvalidPassword
        else:
            return True
