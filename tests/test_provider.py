#!/usr/bin/env python
# encoding: utf-8
from translate.providers import MyMemoryProvider


def test_provider_mymemory_languages_attribute():
    from_lang = 'zh'
    to_lang = 'en'
    provider = MyMemoryProvider(to_lang=to_lang, from_lang=from_lang, headers={})
    expected = '{}|{}'.format(from_lang, to_lang)
    assert provider.languages == expected


def test_provider_mymemory_default_email():
    provider = MyMemoryProvider(to_lang='en', headers={})
    assert provider.email == ''


def test_provider_mymemory_valid_email():
    valid_email = 'test@valid-email.com'
    provider = MyMemoryProvider(to_lang='en', headers={}, email=valid_email)
    assert provider.email == valid_email
