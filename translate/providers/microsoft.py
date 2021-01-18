#!/usr/bin/env python
# encoding: utf-8
from datetime import timedelta
from datetime import datetime

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

    def _make_request(self, text):
        self.headers.update({"Ocp-Apim-Subscription-Key": self.secret_access_key})
        if self.region is not None:
            self.headers.update({"Ocp-Apim-Subscription-Region": "westeurope"})

        params = {
                'to': self.to_lang,
                'api-version': '3.0'
        }

        data = [{
                'text': text
        }]

        if self.from_lang != TRANSLATION_FROM_DEFAULT:
            params['from'] = self.from_lang

        response = requests.post(self.base_url, params=params, headers=self.headers, json=data)

        return json.loads(response.text)

    def get_translation(self, text):
        data = self._make_request(text)

        if "error" in data:
            raise TranslationError(data["error"]["message"])

        return data[0]["translations"][0]["text"]
