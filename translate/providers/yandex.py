import requests
import json

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

    def __init__(self, to_lang, from_lang=TRANSLATION_FROM_DEFAULT, secret_access_key=None, base_url=None, folder_id=None, is_iam=False, **kwargs):
        super().__init__(to_lang, from_lang=from_lang, secret_access_key=secret_access_key, folder_id=folder_id, **kwargs)
        if base_url:
            self.base_url = base_url
        self.folder_id = folder_id
        self.is_iam = is_iam

    def _make_request(self, text):
        body = {
            "targetLanguageCode": self.to_lang,
            "texts": [text],  # Yandex API expects texts as an array
        }

        if self.folder_id:
            body["folderId"] = self.folder_id

        if self.from_lang != TRANSLATION_FROM_DEFAULT:
            body["sourceLanguageCode"] = self.from_lang

        headers = {
            "Content-Type": "application/json",
        }

        if self.is_iam:
            headers["Authorization"] = "Bearer {0}".format(self.secret_access_key)
        else:
            headers["Authorization"] = "Api-Key {0}".format(self.secret_access_key)

        response = self.session.post(
            self.base_url,
            json=body,
            headers=headers,
        )
        response.raise_for_status()
        return json.loads(response.text)

    def get_translation(self, text):
        try:
            data = self._make_request(text)

            if "translations" in data and len(data["translations"]) > 0:
                return data["translations"][0]["text"]
            else:
                raise TranslationError("No translation found in response")
        except requests.HTTPError as e:
            raise TranslationError("HTTP error occurred: {0}".format(str(e)))
        except (KeyError, IndexError) as e:
            raise TranslationError("Invalid response format: {0}".format(str(e)))
        except Exception as e:
            raise TranslationError(str(e))        

