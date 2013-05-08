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
from subprocess import Popen, PIPE, check_output
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

    def test_translate_With_multiple_sentences(self):
        translator = Translator(to_lang="zh")
        translation = translator.translate("yes. no.")
        self.assertIn(u'是。', translation)
        self.assertIn(u'没有。', translation)

class CommandLineTest(TestCase):
    def test_command_line_take_zh_as_default_language(self):
        result = check_output("translate why".split())
        self.assertIn(u'为什么', result.decode("utf-8"))
        
    def test_command_line_take_string_arg(self):
        result = check_output(["translate", 'This is a pen.'])
        self.assertIn(u'这是一支钢笔。', result.decode("utf-8").splitlines())
        
    def test_command_line_take_multiple_args(self):
        result = check_output(["translate", 'one', 'two'])
        self.assertIn(u'一', result.decode("utf-8").splitlines())
        self.assertIn(u'二', result.decode("utf-8").splitlines())
        
    def test_command_line_to_language(self):
        result = check_output(["translate", '--to', 'zh-TW', 'love'])
        self.assertIn(u'愛', result.decode("utf-8").splitlines())

    def test_command_line_from_language(self):
        result = check_output(["translate", '--from', 'ja', '美'])
        self.assertIn(u'美女', result.decode("utf-8").splitlines())
