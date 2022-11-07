#!/usr/bin/env python
# encoding: utf-8

import requests
import json

from .base import BaseProvider
from ..constants import TRANSLATION_FROM_DEFAULT
from ..exceptions import TranslationError

class MicrosoftProvider(BaseProvider):
    '''
    @MicrosoftProvider: This is a integration with Microsoft Translator API.
    Website: http://docs.microsofttranslator.com
    Documentation: http://docs.microsofttranslator.com/text-translate.html
    '''
    name = 'Microsoft'
    base_url = 'https://api.cognitive.microsofttranslator.com/translate'
    session = None

    def _make_request(self, text):
        self.headers.update({"Ocp-Apim-Subscription-Key": self.secret_access_key})
        self.headers.update({"Ocp-Apim-Subscription-Region": self.region or "westeurope"})
        self.headers.update({"Content-type": "application/json"})

        params = {
                'to': self.to_lang,
                'api-version': '3.0'
        }

        data = [{
                'text': text
        }]

        if self.from_lang != TRANSLATION_FROM_DEFAULT:
            params['from'] = self.from_lang

        if self.session is None:
            self.session = requests.Session()
        response = self.session.post(self.base_url, params=params, headers=self.headers, json=data)
        response.raise_for_status()

        return json.loads(response.text)

    def get_translation(self, text):
        data = self._make_request(text)

        if "error" in data:
            raise TranslationError(data["error"]["message"])

        return data[0]["translations"][0]["text"]
