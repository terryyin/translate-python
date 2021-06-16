#!/usr/bin/env python
# encoding: utf-8
import requests
import json

from .base import BaseProvider
from ..exceptions import TranslationError


class LibreProvider(BaseProvider):
    """
    @LibreProvider: This is a integration with LibreTranslate Translator API.
    Website: https://libretranslate.com/
    Documentation: https://libretranslate.com/docs/
    Github: https://github.com/uav4geo/LibreTranslate
    """

    name = "Libre"

    def _make_request(self, text):
        params = {
            "api_key": self.secret_access_key,
            "target": self.to_lang,
            "q": text,
            "source": self.from_lang,
        }

        response = requests.post(
            self.base_url, params=params, headers=self.headers, json=[{}]
        )
        return response.json()

    def get_translation(self, text):
        if self.base_url == "":
            raise TranslationError(
                """
                Please provide a base_url in constructor
                for example,
                translator = Translator(to_lang = "en" , base_url = "http://localhost:5000/")
            """
            )
        data = self._make_request(text)

        if "error" in data:
            raise TranslationError(data["error"])

        return data["translatedText"]
