#!/usr/bin/env python
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <terry.yinzhe@gmail.com> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return to Terry Yin.
#
# The idea of this is borrowed from <mort.yao@gmail.com>'s brilliant work
#    https://github.com/soimort/google-translate-cli
# He uses "THE BEER-WARE LICENSE". That's why I use it too. So you can buy him a 
# beer too.
# ----------------------------------------------------------------------------
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
