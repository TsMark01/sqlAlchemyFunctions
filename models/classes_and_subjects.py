from datetime import datetime
from sqlalchemy import Column, String, Integer

import sys
sys.path.append("..")
from global_base import Base

class Classes_and_subjects(Base):
    __tablename__ = "classes_and_subjects"
    id = Column(Integer, autoincrement=True, primary_key=True)
    d_class = Column(Integer, primary_key=True)
    subject = Column(String(length=100), nullable=False, index=True)
    topic = Column(String(length=100), nullable=True, index=True)


