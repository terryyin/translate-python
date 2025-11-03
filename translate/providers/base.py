#!/usr/bin/env python
# encoding: utf-8

from abc import ABCMeta, abstractmethod
import requests

from ..constants import TRANSLATION_FROM_DEFAULT


class BaseProvider:
    __metaclass__ = ABCMeta

    name = ''
    base_url = ''

    def __init__(self, to_lang, from_lang=TRANSLATION_FROM_DEFAULT, secret_access_key=None, region=None, folder_id=None, **kwargs):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebit/535.19'
                                      '(KHTML, like Gecko) Chrome/18.0.1025.168 Safari/535.19'}
        self.from_lang = from_lang
        self.to_lang = to_lang
        self.secret_access_key = secret_access_key
        self.region = region
        self.kwargs = kwargs
        self.session = requests.Session()

    @abstractmethod
    def get_translation(self, params):
        return NotImplemented('Please Implement this method')
