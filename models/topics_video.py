from datetime import datetime
from sqlalchemy import Column, String, Boolean, Integer, TIMESTAMP, BigInteger

import sys
sys.path.append("..")
from models.global_base import Base

class Topics_video(Base):
    __tablename__ = "topics_video"
    id = Column(Integer, autoincrement=True, primary_key=True)
    d_class = Column(Integer, primary_key=True)
    subject = Column(String(length=100), nullable=False, index=True)
    topic = Column(String(length=100), nullable=True, index=True)


