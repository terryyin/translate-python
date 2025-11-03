#!/usr/bin/env python
# encoding: utf-8
try:
    from unittest import mock
except Exception:
    import mock

from translate.providers import MyMemoryProvider, MicrosoftProvider, YandexProvider


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

@mock.patch('requests.Session.post')
def test_provider_yandex_make_request(mock_requests_post):
    class MockResponse:
        text = '{"translations": [{"text": "test translation"}]}'
        def raise_for_status(self):
            return False

    mock_requests_post.return_value = MockResponse()
    provider = YandexProvider(to_lang='en', secret_access_key='secret', folder_id='some_id')
    result = provider.get_translation('test')
    assert mock_requests_post.called
    assert result == 'test translation'

    args, kwargs = mock_requests_post.call_args
    assert 'Authorization' in kwargs['headers']
    assert kwargs['headers']['Authorization'] == 'Api-Key secret'
    assert kwargs['json']['folderId'] == 'some_id'
    assert kwargs['json']['targetLanguageCode'] == 'en'
    assert kwargs['json']['texts'] == ['test']  # Yandex API expects texts as array


@mock.patch('requests.Session.post')
def test_provider_yandex_autodetect(mock_requests_post):
    class MockResponse:
        text = '{"translations": [{"text": "translated text"}]}'
        def raise_for_status(self):
            return False

    mock_requests_post.return_value = MockResponse()
    provider = YandexProvider(to_lang='fr', secret_access_key='secret')
    result = provider.get_translation('hello')
    assert result == 'translated text'

    args, kwargs = mock_requests_post.call_args
    # Should not include sourceLanguageCode when autodetect
    assert 'sourceLanguageCode' not in kwargs['json']


@mock.patch('requests.Session.post')
def test_provider_yandex_explicit_from_lang(mock_requests_post):
    class MockResponse:
        text = '{"translations": [{"text": "bonjour"}]}'
        def raise_for_status(self):
            return False

    mock_requests_post.return_value = MockResponse()
    provider = YandexProvider(to_lang='fr', from_lang='en', secret_access_key='secret')
    result = provider.get_translation('hello')
    assert result == 'bonjour'

    args, kwargs = mock_requests_post.call_args
    assert kwargs['json']['sourceLanguageCode'] == 'en'


@mock.patch('requests.Session.post')
def test_provider_yandex_iam_token(mock_requests_post):
    class MockResponse:
        text = '{"translations": [{"text": "test"}]}'
        def raise_for_status(self):
            return False

    mock_requests_post.return_value = MockResponse()
    provider = YandexProvider(to_lang='en', secret_access_key='iam_token', is_iam=True)
    provider.get_translation('test')

    args, kwargs = mock_requests_post.call_args
    assert kwargs['headers']['Authorization'] == 'Bearer iam_token'


@mock.patch('requests.Session.post')
def test_provider_yandex_error_handling(mock_requests_post):
    import requests
    class MockResponse:
        text = '{"error": {"message": "Invalid API key"}}'
        def raise_for_status(self):
            raise requests.HTTPError("401 Client Error")

    mock_requests_post.return_value = MockResponse()
    provider = YandexProvider(to_lang='en', secret_access_key='invalid_key')
    
    from translate.exceptions import TranslationError
    import pytest
    with pytest.raises(TranslationError):
        provider.get_translation('test')
