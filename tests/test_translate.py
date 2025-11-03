#!/usr/bin/env python
# encoding: utf-8
try:
    from unittest import mock
except Exception:
    import mock

import pytest

from translate import Translator
from translate.exceptions import InvalidProviderError, TranslationError
from translate.providers import MyMemoryProvider

from .vcr_conf import vcr


def test_tranlate_with_invalid_provider():
    with pytest.raises(InvalidProviderError) as error:
        Translator(to_lang='en', provider='invalid_provider')

    assert 'Provider class invalid. Please check providers list below:' in str(error.value)


def test_tranlate_with_valid_provider():
    translator = Translator(to_lang='en', provider='mymemory')
    assert isinstance(translator.provider, MyMemoryProvider)


def test_tranlate_with_provider_extra_argument():
    # Case from MyMemoryProvider extra argument
    email = 'test@test.com'
    translator = Translator(to_lang='en', email=email)
    assert translator.provider.email == email


@vcr.use_cassette
def test_tranlate_english_to_english():
    translator = Translator(to_lang='en', from_lang='en')
    translation = translator.translate('why')
    assert 'why' == translation


@vcr.use_cassette
def test_translate_english_to_chinese_traditional():
    translator = Translator(to_lang='zh-TW', from_lang='en')
    translation = translator.translate('hello world')
    assert u'你好，世界' == translation


@vcr.use_cassette
def test_translate_english_to_portuguese():
    translator = Translator(to_lang='pt-BR', from_lang='en')
    translation = translator.translate('hello world')
    assert u'olá mundo' == translation


@vcr.use_cassette
def test_translate_english_to_chinese_simplified():
    translator = Translator(to_lang='zh-CN', from_lang='en')
    translation = translator.translate('hello world')
    assert u'你好，世界' == translation


@vcr.use_cassette
def test_translate_with_quote():
    translator = Translator(to_lang='zh', from_lang='en')
    translation = translator.translate("What is 'yinyang'?")
    assert u'什么是\u201c阴阳\u201d？' == translation


@vcr.use_cassette
def test_translate_with_multiple_sentences():
    translator = Translator(to_lang='zh', from_lang='en')
    translation = translator.translate('yes or no')
    assert u'是或否' in translation


@vcr.use_cassette
def test_translate_with_HTTPError():
    import requests
    t = Translator(to_lang='de', from_lang='en', provider='mymemory')
    t.provider.base_url += '-nonsense'
    with pytest.raises(requests.HTTPError) as error:
        t.translate('hello')
    assert '404' in str(error)


@vcr.use_cassette
def test_translate_with_status_error():
    import requests
    t = Translator(to_lang='de', from_lang='en', provider='mymemory', email='invalid')
    with pytest.raises((TranslationError, requests.HTTPError)) as error:
        t.translate('hello again!')
    assert 'INVALID EMAIL' in str(error).upper()


@mock.patch('requests.Session.get')
def test_tranlate_taking_secondary_match(mock_get, main_translation_not_found):
    import requests
    mock_response = mock.Mock()
    mock_response.raise_for_status = mock.Mock()
    mock_response.json.return_value = main_translation_not_found
    mock_get.return_value = mock_response
    translator = Translator(to_lang='zh-TW', from_lang='en')
    translation = translator.translate('unknown')
    assert translation == '未知'
