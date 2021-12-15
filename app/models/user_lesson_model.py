from sqlalchemy.orm import backref, relationship
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import (
    Boolean,
    Integer
)
from app.services.helper import BaseModel


@dataclass
class UserLessonModel(db.Model, BaseModel):

    id: int
    user_id: int
    lesson_id: str
    finished: bool

    __tablename__ = "user_lesson"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, db.ForeignKey('users.id'), nullable=False)
    lesson_id = Column(Integer, db.ForeignKey('lessons.id') ,nullable=False)
    finished = Column(Boolean, nullable=False, default=False)

    user = relationship("UserModel", backref=backref("user_lesson", cascade="all, delete-orphan"))
    lesson = relationship("LessonModel", backref=backref("users_lessons", cascade="all, delete-orphan"))