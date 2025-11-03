import requests

from .base import BaseProvider
from ..constants import TRANSLATION_FROM_DEFAULT
from ..exceptions import TranslationError

class YandexProvider(BaseProvider):
    '''
    @YandexProvider: This is a integration with Yandex Translate API.
    Website: https://translate.yandex.com/
    Documentation: https://yandex.cloud/en/docs/translate
    '''
    name = "Yandex"
    base_url = "https://translate.api.cloud.yandex.net/translate/v2/translate"
    session = None

    def __init__(self, to_lang, from_lang=None, secret_access_key=None, base_url=None, folder_id=None, is_iam=False, **kwargs):
        super().__init__(to_lang)
        self.from_lang = from_lang
        self.base_url = base_url
        self.api = secret_access_key
        self.folder_id = folder_id # Folders used by Yandex API
        self.is_iam = is_iam # Yandex can authorise us using API or IAM tokens

    def get_translation(self, text):
        is_autodetect = False
        if self.from_lang in ('autodetect', None):
            self.from_lang = None 
            is_autodetect = True # We can send Yandex nothing if we want it to detect language automatically

        try:
            body = {
                "targetLanguageCode": self.to_lang,
                "texts": text,
                "folderId": self.folder_id,
            }

            if not is_autodetect:
                body["sourceLanguageCode"] = self.from_lang # Inserting source language if we're not going to autodetect it

            headers = {
                "Content-Type": "application/json",
            }

            if self.is_iam:
                headers["Authorization"] = "Bearer {0}".format(self.api) # Passing to Yandex our IAM-token
            else:
                headers["Authorization"] = "Api-Key {0}".format(self.api) # Passing to Yandex our API-token

            response = self.session.post(
                self.base_url,
                json=body,
                headers=headers,
            )

            return response.text
        except Exception as e:
            raise TranslationError(e)        

