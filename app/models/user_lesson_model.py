from sqlalchemy.orm import backref, relationship
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import (
    Boolean,
    Integer
)


@dataclass
class UserLessonModel(db.Model):

    lesson: dict
    finished: bool

    __tablename__ = "user_lesson"

    user_id = Column(Integer, db.ForeignKey('users.id'), primary_key=True)
    lesson_id = Column(Integer, db.ForeignKey('lessons.id') , primary_key=True)
    finished = Column(Boolean, nullable=False, default=False)

    user = relationship("UserModel", backref=backref("user_lesson", cascade="all, delete-orphan"))
    lesson = relationship("LessonModel", backref=backref("user_lesson", cascade="all, delete-orphan"))