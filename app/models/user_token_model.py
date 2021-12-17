from app.configs.database import db
from dataclasses import dataclass
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import (
    DateTime,
    Integer,
    String
)


@dataclass
class UserTokenModel(db.Model):

    id: int
    user_id: int
    token: str
    token_expire: datetime

    __tablename__ = "user_token"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, db.ForeignKey('users.id'), nullable=False)
    token = Column(String, nullable=False)
    token_expire = Column(DateTime, nullable=False)