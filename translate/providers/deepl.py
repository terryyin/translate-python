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
    base_free_url = 'https://api-free.deepl.com/v2/translate'
    base_pro_url = 'https://api.deepl.com/v2/translate'
    session = None

    def __init__(self, **kwargs):
        try:
            super().__init__(**kwargs)
        except TypeError:
            super(DeeplProvider, self).__init__(**kwargs)
        self.pro = self.kwargs.get('pro', False)
        self.base_url = self.base_pro_url if self.pro else self.base_free_url
        self.headers.update({'Authorization': f'DeepL-Auth-Key {self.secret_access_key}'})
        
    def _make_request(self, text):
        params = {
            'target_lang': self.to_lang,
            'text': text
        }

        if self.from_lang != TRANSLATION_FROM_DEFAULT:
            params['source_lang'] = self.from_lang

        if self.session is None:
            self.session = requests.Session()
        response = self.session.post(self.base_url, params=params, headers=self.headers)
        response.raise_for_status()
        return json.loads(response.text)

    def get_translation(self, text):
        data = self._make_request(text)

        if "error" in data:
            raise TranslationError(data["error"]["message"])

        return data["translations"][0]["text"]
