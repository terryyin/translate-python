#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
from unittest import TestCase
from subprocess import Popen, PIPE
from translate import Translator
import sys

decode = [lambda x:x, lambda x:x.decode("utf-8")][sys.version_info.major>2] 

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


class CommandLineTest(TestCase):
    def test_command_line_take_zh_as_default_language(self):
        self.shell = Popen("translate why".split(), stdin = PIPE, stdout = PIPE, stderr = PIPE)
        stdout, stderr = self.shell.communicate("")
        self.assertEqual('', decode(stderr))
        self.assertIn('为什么', decode(stdout))
        
