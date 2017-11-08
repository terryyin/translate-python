#!/usr/bin/env python
# encoding: utf-8
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <terry.yinzhe@gmail.com> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return to Terry Yin.
from textwrap import wrap

import requests


TRANSLATION_API_MAX_LENGHT = 1000


class Translator:
    def __init__(self, to_lang, from_lang='en'):
        self.from_lang = from_lang
        self.to_lang = to_lang
        self.base_url = 'http://mymemory.translated.net/api/get'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19\
                                       (KHTML, like Gecko) Chrome/18.0.1025.168 Safari/535.19'}

    def _get_translation(self, text):
        languages = '{}|{}'.format(self.from_lang, self.to_lang)
        params = {'q': text, 'langpair': languages}
        response = requests.get(self.base_url, params=params, headers=self.headers)
        data = response.json()

        translation = data['responseData']['translatedText']
        if translation:
            return translation
        else:
            matches = data['matches']
            next_best_match = next(match for match in matches)
            return next_best_match['translation']

    def translate(self, text):
        if self.from_lang == self.to_lang:
            return text
        text_list = wrap(text, TRANSLATION_API_MAX_LENGHT, replace_whitespace=False)
        return ' '.join(self._get_translation(text) for text in text_list)
