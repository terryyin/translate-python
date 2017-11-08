#!/usr/bin/env python
# encoding: utf-8
import sys

from translate.main import main

from .vcr_conf import vcr


@vcr.use_cassette
def test_main_take_zh_as_default_language():
    sys.argv = ['hello', 'world']
    result = main()
    assert '你好，世界' == result


@vcr.use_cassette
def test_main_to_language():
    sys.argv = ['-t', 'zh-TW', 'love']
    result = main()
    assert '爱' == result


@vcr.use_cassette
def test_main_from_language():
    sys.argv = ['--from', 'ja', '美']
    result = main()
    assert '美' == result
