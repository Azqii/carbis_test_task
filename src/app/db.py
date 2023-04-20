import enum
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, Column, String, Integer, Enum

Base = declarative_base()

engine = create_engine("sqlite:///settings.db")


class LanguageEnum(enum.Enum):
    en = "en"
    ru = "ru"


class SettingsModel(Base):
    """Модель настроек"""
    __tablename__ = "settings"

    id = Column(Integer, primary_key=True)
    api_key = Column(String, nullable=True)
    language = Column(Enum(LanguageEnum), default=LanguageEnum.ru, nullable=False)


def create_db() -> None:
    """Создает базу данных с таблицей и записью настроек в ней"""
    Base.metadata.create_all(bind=engine)
    session = get_db_session()
    session.add(SettingsModel())
    session.commit()


def get_db_session():
    """Возвращает сессию с подключением к базе данных"""
    Session = sessionmaker(bind=engine)
    return Session()
