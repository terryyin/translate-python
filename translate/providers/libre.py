#!/usr/bin/env python
# encoding: utf-8
from libretranslatepy import LibreTranslateAPI

from .base import BaseProvider
from ..exceptions import TranslationError

class LibreProvider(BaseProvider):
    """
    @LibreProvider: This is a integration with LibreTranslate translation API.
    Website: https://libretranslate.com/
    Documentation: https://libretranslate.com/docs/
    Github: https://github.com/LibreTranslate/LibreTranslate
    """

    name = "Libre"

    def __init__(self, to_lang, from_lang='en', secret_access_key=None, region=None, base_url=None, **kwargs):
        super().__init__(to_lang)
        self.from_lang = from_lang
        self.base_url = base_url
        self.api = LibreTranslateAPI(base_url, secret_access_key)

    def get_translation(self, text):
        if self.from_lang == 'autodetect':
            from_lang = self.api.detect(text)[0]['language']
        else:
            from_lang = self.from_lang

        try:
            return self.api.translate(text, from_lang, self.to_lang)
        except Exception as e:
            raise TranslationError(e)

