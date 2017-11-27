#!/usr/bin/env python
# encoding: utf-8
import pytest
from click.testing import CliRunner


@pytest.fixture
def cli_runner():
    return CliRunner()


@pytest.fixture
def main_translation_not_found():
    return {
        'responseData': {
            'translatedText': '',
            'match': 0
        },
        'quotaFinished': False,
        'responseDetails': '',
        'responseStatus': 200,
        'responderId': '236',
        'matches': [
            {
                'id': '437872254',
                'segment': 'unknown',
                'translation': '未知',
                'quality': '80',
                'reference': None,
                'usage-count': 22,
                'subject': 'All',
                'created-by': 'MateCat',
                'last-updated-by': 'MateCat',
                'create-date': '2016-09-30 08:10:55',
                'last-update-date': '2016-09-30 08:10:55',
                'match': 1
            }
        ]
    }
