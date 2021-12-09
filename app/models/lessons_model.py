from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import (
    Integer,
    String,
    Boolean,
    Text,
)


@dataclass
class LessonModel(db.Model):

    id: int
    title: str
    description: str
    url_video: str
    is_premium: bool
    category: dict

    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    url_video = Column(String, nullable=False)
    is_premium = Column(Boolean, nullable=False)
    category_id = Column(Integer, db.ForeignKey('categories.id'), nullable=False)

    category = relationship('CategoryModel', backref="lessons", uselist=False)