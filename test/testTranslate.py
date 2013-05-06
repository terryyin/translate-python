#!/usr/bin/evn python
# -*- coding: utf-8 -*-
from unittest import TestCase
from translate import Translator

class TestTranslate(TestCase):

    def test_tranlate_english_to_englsih(self):
        translator = Translator(to_lang="en")
        translation = translator.translate("why")
        self.assertEqual(u"why", translation)
		
    def test_translate_english_to_Chinese(self):
        translator = Translator(to_lang="zh")
        translation = translator.translate("why")
        self.assertEqual(u"为什么",translation)
		
    def test_translate_english_to_Chinese_Simple_sentence(self):
        translator = Translator(to_lang="zh")
        translation = translator.translate("why stop?")
        self.assertEqual(u"为什么要停止呢？",translation)

    def test_translate_With_Quote(self):
        translator = Translator(to_lang="en")
        translation = translator.translate("What is \"yinyang\"?")
        self.assertEqual(u"What is \"yinyang\"?",translation)
