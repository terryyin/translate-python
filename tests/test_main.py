#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals
try:
    from unittest import mock
except Exception:
    import mock

from translate.main import main

from .vcr_conf import vcr


@vcr.use_cassette
def test_main_language_to_translate_required(cli_runner):
    result = cli_runner.invoke(main, ['hello', 'world'], input='zh')
    assert 'Translate to []: zh\n你好，世界\n' == result.output


@vcr.use_cassette
def test_main_to_language(cli_runner):
    result = cli_runner.invoke(main, ['-t', 'zh-TW', 'love'])
    assert '爱\n' == result.output


@vcr.use_cassette
def test_main_from_language(cli_runner):
    result = cli_runner.invoke(main, ['--from', 'ja', '--to', 'zh', '美'])
    assert '美\n' == result.output


@mock.patch('translate.main.__version__', '0.0.0')
def test_main_get_vesion(cli_runner):
    result = cli_runner.invoke(main, ['--version'])
    assert 'translate, version 0.0.0\n' == result.output
