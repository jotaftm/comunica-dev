from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import (
    Boolean,
    Integer
)


@dataclass
class UserLessonModel(db.Model):

    id: int
    user_id: int
    lesson_id: str
    finished: bool

    __tablename__ = "user_lesson"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, db.ForeignKey('users.id'), nullable=False)
    lesson_id = Column(Integer, db.ForeignKey('lessons.id') ,nullable=False)
    finished = Column(Boolean, nullable=False)