#!/usr/bin/env python
# encoding: utf-8
try:
    from unittest import mock
except Exception:
    import mock

from translate.providers import MyMemoryProvider, MicrosoftProvider, LibreProvider


def test_provider_mymemory_languages_attribute():
    from_lang = 'zh'
    to_lang = 'en'
    provider = MyMemoryProvider(to_lang=to_lang, from_lang=from_lang, headers={})
    expected = '{}|{}'.format(from_lang, to_lang)
    assert provider.languages == expected


def test_provider_mymemory_default_email():
    provider = MyMemoryProvider(to_lang='en', headers={})
    assert provider.email == ''


@mock.patch('requests.Session.get')
def test_provider_mymemory_make_request_with_valid_email(mock_requests):
    mock_requests.return_value.json.return_value = {}
    valid_email = 'test@valid-email.com'
    provider = MyMemoryProvider(to_lang='de', headers={}, email=valid_email)
    provider._make_request('test')
    assert mock_requests._mock_call_args[1]['params']['de'] == valid_email == provider.email


@mock.patch('requests.Session.post')
def test_provider_microsoft_make_request(mock_requests_post):
    class MockResponse:
        text = '"dummyjson"'
        def raise_for_status(self):
            return False

    mock_requests_post.return_value = MockResponse()
    provider = MicrosoftProvider(to_lang='en', headers={}, secret_access_key='secret')
    provider._make_request('test')
    assert mock_requests_post.called
