#!/usr/bin/env python
# encoding: utf-8
import requests

from .base import BaseProvider
from ..exceptions import TranslationError


class MyMemoryProvider(BaseProvider):
    '''
    @MyMemoryProvider: This is a integration with Translated MyMemory API.
    Follow Informations:
      Website: https://mymemory.translated.net/
      Documentation: https://mymemory.translated.net/doc/spec.php

    Usage Tips: Use a valid email instead of the default.
        With a valid email you get 10 times more words/day to translate.
    For further information checkout:
    http://mymemory.translated.net/doc/usagelimits.php
                                                    Tips from: @Bachstelze
    '''
    name = 'MyMemory'
    base_url = 'http://api.mymemory.translated.net/get'
    session = None

    def __init__(self, **kwargs):
        try:
            super().__init__(**kwargs)
        except TypeError:
            super(MyMemoryProvider, self).__init__(**kwargs)

        self.email = kwargs.get('email', '')
        self.languages = '{}|{}'.format(self.from_lang, self.to_lang)

    def _make_request(self, text):
        params = {'q': text, 'langpair': self.languages}
        if self.email:
            params['de'] = self.email

        if self.session is None:
            self.session = requests.Session()
        response = self.session.get(self.base_url, params=params, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_translation(self, text):
        data = self._make_request(text)

        translation = data['responseData']['translatedText']
        if data['responseStatus'] != 200:
            e = TranslationError(translation)
            e.json = data
            raise e
        if translation:
            return translation
        else:
            matches = data['matches']
            next_best_match = next(match for match in matches)
            return next_best_match['translation']
