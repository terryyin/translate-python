#!/usr/bin/env python
# encoding: utf-8
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <terry.yinzhe@gmail.com> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return to Terry Yin.
from textwrap import wrap

from .exceptions import InvalidProviderError
from .providers import MyMemoryProvider


TRANSLATION_API_MAX_LENGHT = 1000


class Translator:
    default_provider = MyMemoryProvider

    def __init__(self, to_lang, from_lang='en', provider_class=None, secret_access_key=None):
        self.from_lang = from_lang
        self.to_lang = to_lang
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19\
                                  (KHTML, like Gecko) Chrome/18.0.1025.168 Safari/535.19'}
        provider_class = provider_class or self.default_provider

        if not hasattr(provider_class, 'get_translation'):
                raise InvalidProviderError('Provider class invalid. Please check providers list.')

        self.provider = provider_class(
            from_lang=from_lang,
            to_lang=to_lang,
            headers=headers,
            secret_access_key=secret_access_key
        )

    def translate(self, text):
        if self.from_lang == self.to_lang:
            return text

        text_list = wrap(text, TRANSLATION_API_MAX_LENGHT, replace_whitespace=False)
        return ' '.join(self.provider.get_translation(text_wraped) for text_wraped in text_list)
