from app.configs.database import db
from dataclasses import dataclass
from datetime import datetime
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import (
    Integer,
    String,
    DateTime,
    Boolean,
)
from sqlalchemy.orm import validates
import re
from app.exc.leads_exc import InvalidEmailFormat


@dataclass
class LeadModel(db.Model):

    id: int
    email: str
    name: str
    created_at: datetime
    is_user: bool

    __tablename__ = "leads"

    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False, unique=True)
    name = Column(String(100), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    is_user = Column(Boolean, nullable=False)

    @validates('email')
    def validate_email(self, key, email):
        try:
            pattern = "/^[a-z0-9.]+@[a-z0-9]+\.[a-z]+\.([a-z]+)?$/i"
            email_type = type(email) == str
            correct_email_format = re.fullmatch(pattern, email)
        except:
            raise InvalidEmailFormat("O email deve ser do tipo string e deve conter @")
        
        return email
