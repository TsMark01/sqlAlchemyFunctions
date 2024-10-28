from sqlalchemy import create_engine
import sys
sys.path.append("..")
from global_config import SQLALCHEMY_DATABASE_URL
from global_base import Base

def create_all():
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    Base.metadata.create_all(bind=engine)

    print("tables created")


create_all()