#!/usr/bin/env python
# encoding: utf-8
from translate import Translator
try:
    from unittest import mock
except Exception:
    import mock

from .vcr_conf import vcr


@vcr.use_cassette
def test_tranlate_english_to_english():
    translator = Translator(to_lang='en')
    translation = translator.translate('why')
    assert 'why' == translation


@vcr.use_cassette
def test_translate_english_to_chinese_traditional():
    translator = Translator(to_lang='zh-TW')
    translation = translator.translate('hello world')
    assert u'你好，世界' == translation


@vcr.use_cassette
def test_translate_english_to_portuguese():
    translator = Translator(to_lang='pt-BR')
    translation = translator.translate('hello world')
    assert u'olá mundo' == translation


@vcr.use_cassette
def test_translate_english_to_chinese_simplified():
    translator = Translator(to_lang='zh-CN')
    translation = translator.translate('hello world')
    assert u'你好，世界' == translation


@vcr.use_cassette
def test_translate_with_quote():
    translator = Translator(to_lang='zh')
    translation = translator.translate("What is 'yinyang'?")
    assert u'什么是“阴阳”？' == translation


@vcr.use_cassette
def test_translate_with_multiple_sentences():
    translator = Translator(to_lang='zh')
    translation = translator.translate('yes or no')
    assert u'是或否' in translation


@mock.patch('requests.get')
def test_tranlate_taking_secondary_match(mock_requests, main_translation_not_found):
    mock_requests.return_value.json.return_value = main_translation_not_found
    translator = Translator(to_lang='zh-TW')
    translation = translator.translate('unknown')
    assert '未知' == translation
