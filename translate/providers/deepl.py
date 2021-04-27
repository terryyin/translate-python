#!/usr/bin/env python
# encoding: utf-8
import requests
import json

from .base import BaseProvider
from ..constants import TRANSLATION_FROM_DEFAULT
from ..exceptions import TranslationError


class DeeplProvider(BaseProvider):
    '''
    @DeeplProvider: This is a integration with DeepL Translator API.
    Website: https://www.deepl.com
    Documentation: https://www.deepl.com/docs-api
    '''
    name = 'Deepl'
    base_url = 'https://api-free.deepl.com/v2/translate'

    def _make_request(self, text):
        params = {
            'auth_key': self.secret_access_key,
            'target_lang': self.to_lang,
            'text': text
        }

        if self.from_lang != TRANSLATION_FROM_DEFAULT:
            params['source_lang'] = self.from_lang

        response = requests.post(self.base_url, params=params, headers=self.headers, json=[{}])
        return json.loads(response.text)

    def get_translation(self, text):
        data = self._make_request(text)

        if "error" in data:
            raise TranslationError(data["error"]["message"])

        return data["translations"][0]["text"]
