Tutorial
========

Command Line
------------

In your command-line:

.. code-block:: bash

   $ translate-cli -t zh "This is a pen."

   Translation: 这是一支笔
   -------------------------
   Translated by: MyMemory

Or

.. code-block:: bash

   $ translate-cli -t zh "This is a pen." -o
   这是一支笔


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


Change Default Languages
~~~~~~~~~~~~~~~~~~~~~~~~

In ~/.python-translate.cfg:

.. code-block:: bash

   [DEFAULT]
   from_lang = autodetect
   to_lang = de
   provider = mymemory
   secret_access_key =

The cfg is not for using as a Python module.

or run the command line and follow the steps:

.. code-block:: bash

    $ translate-cli --generate-config-file
    Translate from [autodetect]:
    Translate to: <language you want to translate>
    Provider [mymemory]:
    Secret Access Key []:


The country code, as far as I know, is following https://en.wikipedia.org/wiki/ISO_639-1.

Use As A Python Module
----------------------

::

   In [1]: from translate import Translator
   In [2]: translator= Translator(to_lang="zh")
   In [3]: translation = translator.translate("This is a pen.")
   Out [3]: 这是一支笔

The result is in translation, and it’s usually a unicode string.


Use a different translation provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    In [1]: from translate import Translator
    In [2]: to_lang = 'zh'
    In [3]: secret = '<your secret from Microsoft>'
    In [4]: translator = Translator(provider='microsoft', to_lang=to_lang, secret_access_key=secret)
    In [5]: translator.translate('the book is on the table')
    Out [5]: '碗是在桌子上。'
