
from dataclasses import dataclass
from sqlalchemy import (
    Column,
    String,
    Integer
)

from app.configs.database import db


@dataclass
class CaptchaModel(db.Model):
    url_captcha: str

    __tablename__ = "captchas"

    id = Column(Integer, primary_key=True)
    url_captcha = Column(String, nullable=False)
    captcha_content = Column(String, nullable=False)
