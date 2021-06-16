Providers
=========

Providers are responsible to translate the text


MicrosoftProvider
-----------------

It is a paid provider but it is possible you can create a free account tends a quota of up to 2m of words per day

``MicrosoftProvider`` (located at ``translate.providers``) receives the following options:

to_lang, from_lang='en', secret_access_key

    * ``to_lang``: language you want to translate
    * ``from_lang``: Language of the text being translated  (optional): as default ``autodetect``
    * ``secret_access_key``: oAuth Access Token

for further information abount the provider:

    http://docs.microsofttranslator.com/
    https://azure.microsoft.com/en-us/pricing/details/cognitive-services/translator-text-api/


MyMemory
--------

Is a free provider but very  complete

``MyMemory`` (located at ``translate.providers``) receives the following options:

to_lang, from_lang='en', email

    * ``to_lang``: language you want to translate
    * ``from_lang``: Language of the text being translated  (optional): as default ``autodetect``
    * ``email``: Valid email to increase your translations cote

for further information abount the provider:

    https://mymemory.translated.net/doc/spec.php
    http://mymemory.translated.net/doc/usagelimits.php

LibreTranslate
--------

Free and open source translation provider

``LibreTranslate`` (located at ``translate.providers``) receives the following options:

to_lang, from_lang='en', secret_access_key=None, base_url="https://translate.astian.org/"

    * ``to_lang``: language you want to translate
    * ``from_lang``: Language of the text being translated  (optional): as default ``autodetect``
    * ``secret_access_key``: LibreTranslate API key
	* ``base_url``: LibreTranslate instance url

for further information abount the provider:

    https://libretranslate.com
    http://github.com/LibreTranslate/LibreTranslate
