from dadata import Dadata

from .repository import SettingsRepository
from .db import LanguageEnum


class DadataAPIWrapper:
    def __init__(self):
        self._repository = SettingsRepository()
        self._settings = self._repository.get_settings()

    @property
    def settings(self):
        return self._settings

    def change_api_key(self, api_key: str):
        self._repository.change_api_key(self._settings, api_key)

    def change_language(self, language: str):
        enum_language = LanguageEnum.ru if language == "ru" else LanguageEnum.en
        self._repository.change_language(self._settings, enum_language)

    def suggest(self, query: str, count: int = 10):
        """Возвращает список адресов с информацией для указанного запроса query"""
        with Dadata(self._settings.api_key) as dadata:
            return dadata.suggest(name="address", query=query, language=self._settings.language.value, count=count)
