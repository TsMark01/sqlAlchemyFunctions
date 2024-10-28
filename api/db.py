import sys
from ..models.global_config import SQLALCHEMY_DATABASE_URL
from ..models.global_base import Base

sys.path.append("..")
from sqlalchemy import select, update
from sqlalchemy.orm import sessionmaker
from ..models.d_user import User
from ..models.classes_and_subjects import Classes_and_subjects
from ..models.topics_lessons import Topics_lessons
from sqlalchemy import create_engine

import datetime


class GlobalDb():
    def __init__(self):
        self.engine = create_engine(SQLALCHEMY_DATABASE_URL)
        Base.metadata.create_all(bind=self.engine)
        self.sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def insertuser(self, telegram_id, telegram_username, is_active, is_paid, ref_src, parent_id):
        try:
            with self.sessionmaker() as session:
                newuser = User(
                    telegram_id=telegram_id,
                    telegram_username=telegram_username,
                    created_at=datetime.datetime.utcnow(),
                    updated_at=datetime.datetime.utcnow(),
                    last_active_at=datetime.datetime.utcnow(),
                    is_active=is_active,
                    is_paid=is_paid,
                    ref_src=ref_src,
                    parent_id=parent_id
                )
                session.add(newuser)
                session.commit()
        except Exception as e:
            print(f"Ошибка при вставке пользователя: {e}")

    def checkuser(self, telegram_id):
        try:
            with self.sessionmaker() as session:
                records = session.execute(select(User).where(User.telegram_id == telegram_id))
                user = records.first()
                return user[0] if user else None
        except Exception as e:
            print(f"Ошибка при проверке пользователя: {e}")
            return None

    def update_premium(self, telegram_id):
        try:
            with self.sessionmaker() as session:
                session.execute(
                    update(User).
                    where(User.telegram_id == telegram_id).
                    values(is_paid=True)
                )
                session.commit()
        except Exception as e:
            print(f"Ошибка при обновлении статуса премиума пользователя с айди {telegram_id}: {e}")

    def get_topics_by_class_and_subject(self, d_class: int, subject: str):
        try:
            with self.sessionmaker() as session:
                records = session.execute(
                    select(Classes_and_subjects.topic).
                    where(Classes_and_subjects.d_class == d_class, Classes_and_subjects.subject == subject)
                ).scalars().all()  # Получаем все темы
                return records  # Возвращаем список тем
        except Exception as e:
            print(f"Ошибка при получении тем в классе {d_class}, в предмете {subject}: {e}")
            return [f"Ошибка при получении тем в классе {d_class}, в предмете {subject}: {e}"]

    from sqlalchemy import select

    def get_all_subjects(self, d_class: int):
        try:
            with self.sessionmaker() as session:
                records = session.execute(
                    select(Classes_and_subjects.subject).
                    where(Classes_and_subjects.d_class == d_class).
                    distinct()  # Получаем уникальные предметы
                ).scalars().all()  # Получаем список всех предметов
                return records
        except Exception as e:
            print(f"Ошибка при получении предметов: {e}")
            return [f"Ошибка при получении предметов: {e}"]

    # Функция для получения всех классов
    def get_all_classes(self):
        try:
            with self.sessionmaker() as session:
                records = session.execute(
                    select(Classes_and_subjects.d_class).
                    distinct()  # Получаем уникальные классы
                ).scalars().all()  # Получаем список всех классов
                return records
        except Exception as e:
            print(f"Ошибка при получении классов: {e}")
            return [f"Ошибка при получении классов: {e}"]

    def get_lessons_by_topic(self, topic: str):
        try:
            with self.sessionmaker() as session:
                records = session.execute(
                    select(Topics_lessons.lesson).
                    where(Topics_lessons.topic == topic)
                ).scalars().all()  # Получаем все уроки для указанной темы
                return records  # Возвращаем список уроков
        except Exception as e:
            print(f"Ошибка при получении уроков по теме '{topic}': {e}")
            return [f"Ошибка при получении уроков по теме '{topic}': {e}"]

        # Функция для получения video_url и presentation_url по названию урока

    def get_urls_by_lesson_and_topic(self, lesson: str, topic: str):
        try:
            with self.sessionmaker() as session:
                records = session.execute(
                    select(Topics_lessons.video_url, Topics_lessons.presentation_url).
                    where(Topics_lessons.lesson == lesson, Topics_lessons.topic == topic)
                ).all()  # Получаем все результаты

                # Преобразуем результаты в список
                urls = [(record[0], record[1]) for record in records]
                return urls  # Возвращаем список с video_url и presentation_url
        except Exception as e:
            print(f"Ошибка при получении URL для урока '{lesson}' и темы '{topic}': {e}")
            return [f"Ошибка при получении URL для урока '{lesson}' и темы '{topic}': {e}"]


