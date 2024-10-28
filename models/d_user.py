from datetime import datetime
from sqlalchemy import Column, String, Boolean, Integer, TIMESTAMP, BigInteger

import sys
sys.path.append("..")
from global_base import Base

class User(Base):
    __tablename__ = "d_user"
    id = Column(Integer, autoincrement=True, primary_key=True)
    telegram_id = Column(BigInteger, nullable=False, index=True)
    telegram_username = Column(String(length=100), nullable=True, index=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow(), index=True)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow(), index=True)
    last_active_at = Column(TIMESTAMP, default=datetime.utcnow(), index=True)
    is_active = Column(Boolean, nullable=False, default=True, index=True)
    is_paid = Column(Boolean, nullable=False, default=False, index=True)
    ref_src = Column(String(length=255), nullable=True, index=True)
    parent_id = Column(Integer, nullable=True, index=True)

