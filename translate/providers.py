#!/usr/bin/env python
# encoding: utf-8

from abc import ABCMeta, abstractmethod

import requests


class BaseProvider:
    __metaclass__ = ABCMeta

    base_url = ''

    def __init__(self, to_lang, headers, from_lang='en', secret_access_key=None, **kwargs):
        self.from_lang = from_lang
        self.to_lang = to_lang
        self.headers = headers
        self.secret_access_key = secret_access_key

    @abstractmethod
    def get_translation(self, params):
        return NotImplemented('Please Implement this method')


class MyMemoryProvider(BaseProvider):
    '''
    @MyMemoryProvider: http://mymemory.translated.net
    Usage: Use a valid email instead of the default.
    With a valid email you get 10 times more words/day to translate.
    For further infomations checkout:
    http://mymemory.translated.net/doc/usagelimits.php
    http://mymemory.translated.net/doc/spec.php  Tips from: @Bachstelze
    '''
    base_url = 'http://api.mymemory.translated.net/get'

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
            params['email'] = self.email

        response = requests.get(self.base_url, params=params, headers=self.headers)
        return response.json()

    def get_translation(self, text):
        data = self._make_request(text)

        translation = data['responseData']['translatedText']
        if translation:
            return translation
        else:
            matches = data['matches']
            next_best_match = next(match for match in matches)
            return next_best_match['translation']
