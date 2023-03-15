from .db import get_db_session, Settings, LanguageEnum


class SettingsRepository:
    """Репозиторий запросов к базе данных"""

    def __init__(self):
        self.session = get_db_session()

    def get_settings(self):
        """Возвращает объект с настройками из базы данных"""
        return self.session.query(Settings).get(1)

    def change_api_key(self, settings: Settings, api_key: str) -> None:
        """Изменяет API-ключ в настройках"""
        settings.api_key = api_key
        self.session.commit()

    def change_language(self, settings: Settings, language: LanguageEnum) -> None:
        """Изменяет язык в настройках"""
        settings.language = language
        self.session.commit()
