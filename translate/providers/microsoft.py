#!/usr/bin/env python
# encoding: utf-8
from datetime import timedelta
from datetime import datetime

from lxml import etree
import requests

from .base import BaseProvider
from ..constants import TRANSLATION_FROM_DEFAULT


class AzureAuthClient:
    """
    Provides a client for obtaining an OAuth token from the authentication service
    for Microsoft Translator in Azure Cognitive Services.

    PS:
    token field is used to store the last token obtained from the token service
    the cached token is re-used until the time specified in reuse_token_until.
    """
    base_url = 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken'

    def __init__(self, client_secret):
        self.client_secret = client_secret
        self.token = None
        self.reuse_token_until = None

    def get_access_token(self):
        '''
        Returns an access token for the specified subscription.

        This method uses a cache to limit the number of requests to the token service.
        A fresh token can be re-used during its lifetime of 10 minutes. After a successful
        request to the token service, this method caches the access token. Subsequent
        invocations of the method return the cached token for the next 5 minutes. After
        5 minutes, a new token is fetched from the token service and the cache is updated.
        '''

        if (self.token is None) or (datetime.utcnow() > self.reuse_token_until):
            headers = {'Ocp-Apim-Subscription-Key': self.client_secret}
            response = requests.post(self.base_url, headers=headers)
            response.raise_for_status()

            self.token = response.content
            self.reuse_token_until = datetime.utcnow() + timedelta(minutes=5)

        return self.token.decode('utf-8')


class MicrosoftProvider(BaseProvider):
    '''
    @MicrosoftProvider: This is a integration with Microsoft Translator API.
    Website: http://docs.microsofttranslator.com
    Documentation: http://docs.microsofttranslator.com/text-translate.html
    '''
    name = 'Microsoft'
    base_url = 'http://api.microsofttranslator.com/v2/Http.svc/Translate'

    def _make_request(self, text):
        auth_client = AzureAuthClient(self.secret_access_key)
        access_token = 'Bearer {}'.format(auth_client.get_access_token())
        self.headers.update({"Authorization ": access_token})

        params = {'text': text, 'to': self.to_lang}
        if self.from_lang != TRANSLATION_FROM_DEFAULT:
            params['from'] = self.from_lang

        response = requests.get(self.base_url, params=params, headers=self.headers)

        return response.text

    def get_translation(self, text):
        data = self._make_request(text)

        translation = etree.fromstring(data.encode('utf-8'))
        return translation.text
