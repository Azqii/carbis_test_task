from .db import SettingsModel, LanguageEnum


class SettingsRepository:
    """Репозиторий запросов к базе данных"""

    @staticmethod
    def get_settings(session) -> SettingsModel:
        """Возвращает объект с настройками из базы данных"""
        return session.query(SettingsModel).get(1)

    @staticmethod
    def change_api_key(session, settings: SettingsModel, api_key: str) -> None:
        """Изменяет API-ключ в настройках"""
        settings.api_key = api_key
        session.commit()

    @staticmethod
    def change_language(session, settings: SettingsModel, language: LanguageEnum) -> None:
        """Изменяет язык в настройках"""
        settings.language = language
        session.commit()
