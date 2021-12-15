from dataclasses import dataclass
from sqlalchemy import (
    Column,
    String,
    Integer
)

from app.configs.database import db
from app.services.helper import BaseModel


@dataclass
class CaptchaModel(db.Model, BaseModel):
    url_captcha: str

    __tablename__ = "captchas"

    id = Column(Integer, primary_key=True)
    url_captcha = Column(String, nullable=False)
    captcha_content = Column(String, nullable=False)
