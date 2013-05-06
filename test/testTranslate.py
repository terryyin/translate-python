#!/usr/bin/evn python
# -*- coding: utf-8 -*-
from unittest import TestCase
from translate import Translator

class TestTranslate(TestCase):

    def test_tranlate_english_to_englsih(self):
        translator = Translator(to_lang="en")
        translation = translator.translate("why")
        assert translation == "why"
		
    def xtest_translate_english_to_Chinese(self):
        translator = Translator(to_lang="zh")
        translation = translator.translate("why")
        assert translation == "为什么"
		
