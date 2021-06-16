#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals
import unittest
try:
    from unittest import mock
except Exception:
    import mock

from translate.main import main

from .vcr_conf import vcr

response_template = (
    '\nTranslation: {}\n'
    '-------------------------\n'
    'Translated by: MyMemory\n'
)
deepl_response_template = (
    '\nTranslation: {}\n'
    '-------------------------\n'
    'Translated by: Deepl\n'
)
deepl_secret = 'secret'


@vcr.use_cassette
def test_main_language_to_translate_required(cli_runner):
    result = cli_runner.invoke(main, ['hello', 'world'], input='zh')
    response = response_template.format('你好，世界')
    assert 'Translate to []: zh\n{}'.format(response) == result.output


@vcr.use_cassette
def test_main_to_language(cli_runner):
    result = cli_runner.invoke(main, ['-t', 'zh-TW', 'love'])
    assert response_template.format('爱') == result.output


@vcr.use_cassette
def test_main_to_language_output_only(cli_runner):
    result = cli_runner.invoke(main, ['-t', 'zh-TW', '-o', 'love'])
    assert '爱\n' == result.output


@vcr.use_cassette
def test_main_from_language(cli_runner):
    result = cli_runner.invoke(main, ['--from', 'ja', '--to', 'zh', '美'])
    assert response_template.format('美') == result.output


@mock.patch('translate.main.__version__', '0.0.0')
def test_main_get_vesion(cli_runner):
    result = cli_runner.invoke(main, ['--version'])
    assert 'translate, version 0.0.0\n' == result.output


@unittest.skipIf(deepl_secret == 'secret', 'No authentication token provided for DeepL')
def test_main_deepl_provider(cli_runner):
    result = cli_runner.invoke(main, ['--provider', 'deepl', '--from', 'de', '--to', 'zh', '--secret_access_key', deepl_secret, 'the book is on the table'])
    assert deepl_response_template.format('书在桌上') == result.output
