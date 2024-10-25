import datetime
from sqlalchemy import create_engine
import sys
from global_config import SQLALCHEMY_DATABASE_URL
from models.global_base import Base
sys.path.append("..")
from utils.session import SessionLocal
from sqlalchemy import select, update, text, and_, or_
from sqlalchemy.orm import sessionmaker
from models.d_user import User
from models.topics_video import Topics_video

class GlobalDb():
    def __init__(self):
        self.engine = create_engine(SQLALCHEMY_DATABASE_URL)
        Base.metadata.create_all(bind=self.engine)

        self.sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.session_local = SessionLocal()


    def insertuser(self, telegram_id, telegram_username, created_at, updated_at, last_active_at, is_active, is_paid, ref_src, parent_id):
        newuser = User(
            telegram_id= telegram_id,
            telegram_username=telegram_username,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
            last_active_at=datetime.datetime.utcnow(),
            is_active=is_active,
            is_paid=is_paid,
            ref_src=ref_src,
            parent_id=parent_id
        )

        self.session_local.add(newuser)
        self.session_local.commit()

    def checkuser(self, telegram_id):
        records = self.session_local.execute(select(User).where(User.telegram_id == telegram_id))
        user = records.first()
        self.session_local.close()
        if user == None:
            return None
        else:
            return user[0]

    def update_premium(self, telegram_id):






