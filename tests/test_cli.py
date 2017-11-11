#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals
from subprocess import check_output


def test_command_line_complete():
    # This test is impossible mock because is a subprocess
    result = check_output(
        ["./translate-cli", '--from', 'en', '--to', 'zh-TW',
         "The", "book", "is", "on", "the", "table."]
    )
    assert '碗是在桌子上。\n' in result.decode("utf-8")
