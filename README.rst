=======================
Translate Tool in Python
=======================

Now google has stop providing free translation API. So I have to switch to
http://mymemory.translated.net/, which has a limit for 1000 words/day free
usage (5000 if you register an email). There's also other prodivers can be
choosed from. Please let me know if there's any other better free translation API than we already have.

The default from language is English (en).
The default to language is Simplified Chinese (zh). Of course, you can specify it
in the parameter or command line.

Installation
------------

.. code-block:: bash

   $ pip install translate

Or, you can download the source and

.. code-block:: bash

   $ python setup.py install

Add sudo in the beginning if you met problem.

Usage
-----

In your command-line:

.. code-block:: bash

   $ translate-cli "This is a pen."

   Translation: O livro esta em cima da mesa
   -------------------------
   Translated by: MyMemory

Or

.. code-block:: bash

   $ translate-cli -f zh -t ja -o
   我是谁？

Options
~~~~~~~

.. code-block:: bash

    $ translate-cli --help
    Usage: __main__.py [OPTIONS] TEXT...

      Python command line tool to make on line translations

      Example:

           $ translate-cli -t zh the book is on the table
           碗是在桌子上。

      Available languages:

           https://en.wikipedia.org/wiki/ISO_639-1
           Examples: (e.g. en, ja, ko, pt, zh, zh-TW, ...)

    Options:
      --version                 Show the version and exit.
      --generate-config-file    Generated the config file using a Wizard and exit.
      -f, --from TEXT           Sets the language of the text being translated.
                                The default value is 'autodetect'.
      -t, --to TEXT             Sets the language you want to translate.
      -p, --provider TEXT       Set the provider you want to use. The default
                                value is 'mymemory'.
      --secret_access_key TEXT  Set the secret access key used to get provider
                                oAuth token.
      -o, --output_only         Set to display the translation only.
      --help                    Show this message and exit.

Use As A Python Module
----------------------

.. code-block:: python

   In [1]: from translate import Translator
   In [2]: translator= Translator(to_lang="zh")
   In [3]: translation = translator.translate("This is a pen.")
   Out [3]: 这是一支笔

The result is in translation, and it’s usually a unicode string.

Change Default Languages
------------------------

In ~/.python-translate.cfg:

.. code-block:: bash

   [DEFAULT]
   from_lang = autodetect
   to_lang = de
   provider = mymemory
   secret_access_key =

The cfg is not for using as a Python module.
The country code, as far as I know, is following https://en.wikipedia.org/wiki/ISO_639-1.


Use a different translation provider
------------------------------------

.. code-block:: python

    In [1]: from translate import Translator
    In [2]: to_lang = 'zh'
    In [3]: secret = '<your secret from Microsoft>'
    In [4]: translator = Translator(provider='microsoft', to_lang=to_lang, secret_access_key=secret)
    In [5]: translator.translate('the book is on the table')
    Out [5]: '碗是在桌子上。'

Contribution
------------

Please send pull requests, very much appriciated.

If you find an incorrect translation, one thing you can do is to create an account at http://mymemory.translated.net/ and fix their data.
