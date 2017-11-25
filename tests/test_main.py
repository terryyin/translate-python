#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

from translate.main import main

from .vcr_conf import vcr


@vcr.use_cassette
def test_main_take_zh_as_default_language(cli_runner):
    result = cli_runner.invoke(main, ['hello', 'world'])
    assert '你好，世界\n' == result.output


@vcr.use_cassette
def test_main_to_language(cli_runner):
    result = cli_runner.invoke(main, ['-t', 'zh-TW', 'love'])
    assert '爱\n' == result.output


@vcr.use_cassette
def test_main_from_language(cli_runner):
    result = cli_runner.invoke(main, ['--from', 'ja', '美'])
    assert '美\n' == result.output
