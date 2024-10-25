from datetime import datetime
from sqlalchemy import Column, String, Boolean, Integer, TIMESTAMP, BigInteger

import sys
sys.path.append("..")
from models.global_base import Base

class Topics_video(Base):
    __tablename__ = "topics_video"
    d_class = Column(Integer, primary_key=True)
    subject = Column(String(length=100), nullable=False, index=True)
    telegram_username = Column(String(length=100), nullable=True, index=True)
    topic = Column(String(length=100), nullable=True, index=True)
    video_url = Column(String(length=255), nullable=True, index=True)
    presentation_url = Column(String(length=255), nullable=True, index=True)

