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
from app.exc import InvalidEmailError


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
    is_user = Column(Boolean, nullable=False, default=False)

    @validates('email')
    def validate_email(self, key, email):
        pattern = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not re.fullmatch(pattern, email):
            raise InvalidEmailError
        return email