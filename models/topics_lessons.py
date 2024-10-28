from datetime import datetime
from sqlalchemy import Column, String, Boolean, Integer, TIMESTAMP, BigInteger

import sys
sys.path.append("..")
from global_base import Base

class Topics_lessons(Base):
    __tablename__ = "topics_lessons"
    id = Column(Integer, autoincrement=True, primary_key=True)
    topic = Column(String(length=150), nullable=True, index=True)
    lesson = Column(String(length=150), nullable=True, index=True)
    video_url = Column(String(length=255), nullable=True, index=True)
    presentation_url = Column(String(length=255), nullable=True, index=True)


