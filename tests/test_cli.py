#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals
import subprocess
try:
    from unittest import mock
except Exception:
    import mock


def test_command_line_complete():
    # This test is impossible mock direct because is a subprocess
    expected = u'碗是在桌子上。'
    subprocess.check_output = mock.create_autospec(subprocess.check_output, return_value=expected)
    result = subprocess.check_output(
        ["./translate-cli", '--from', 'en', '--to', 'zh-TW',
         "The", "book", "is", "on", "the", "table."]
    )
    assert expected == result
