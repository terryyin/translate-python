import requests

from .base import BaseProvider
from constants import TRANSLATION_FROM_DEFAULT
from exceptions import TranslationError

class YandexProvider(BaseProvider):
    '''
    @YandexProvider: This is a integration with Yandex Translate API.
    Website: https://translate.yandex.com/
    Documentation: https://yandex.cloud/en/docs/translate
    '''
    name = "Yandex"
    base_url = "https://translate.api.cloud.yandex.net/translate/v2/translate"
    session = None

    def __init__(self, to_lang, from_lang=None, secret_access_key=None, base_url=None, folder_id=None, **kwargs):
        super().__init__(to_lang)
        self.from_lang = from_lang
        self.base_url = base_url
        self.api = secret_access_key
        self.folder_id = folder_id # Folders used by Yandex API

    def get_translation(self, text):
        if self.from_lang == 'autodetect' or None:
            from_lang = None 
            isAutodetect = True # We can send Yandex nothing if we want it to detect language automatically
        else:
            from_lang = self.from_lang

        try:
            body = {
                "targetLanguageCode": self.to_lang,
                "texts": text,
                "folderId": self.folder_id,
            }

            headers = {
                "Content-Type": "application/json",
                "Authorization": "Api-Key {0}".format(self.api),
            }

            response = requests.post(
                "https://translate.api.cloud.yandex.net/translate/v2/translate",
                json=body,
                headers=headers,
            )

            return response.text
        except Exception as e:
            raise TranslationError(e)        

