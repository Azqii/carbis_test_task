from typing import Dict, List

from dadata import Dadata

from .repository import SettingsRepository
from .db import LanguageEnum, SettingsModel


class Settings:
    def __init__(self, session) -> None:
        self._session = session
        self._fields = SettingsRepository.get_settings(session)

    @property
    def fields(self) -> SettingsModel:
        return self._fields

    def change_api_key(self, api_key: str) -> None:
        SettingsRepository.change_api_key(self._session, self._fields, api_key)

    def change_language(self, language: LanguageEnum) -> None:
        SettingsRepository.change_language(self._session, self._fields, language)


class DadataAPIWrapper:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    @property
    def settings(self) -> Settings:
        return self._settings

    def suggest(self, query: str, count: int = 10) -> List[Dict]:
        """Возвращает список адресов с информацией для указанного запроса query"""
        with Dadata(self.settings.fields.api_key) as dadata:
            return dadata.suggest(name="address", query=query, language=self.settings.fields.language.value, count=count)
