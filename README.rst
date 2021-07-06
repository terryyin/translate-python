========================
Translate Tool in Python
========================

|PyPI latest| |PyPI Version| |PyPI License| |Docs| |Travis Build Status|


Translate is a simple but powerful translation tool written in python with with support for
multiple translation providers. By now we offer integration with Microsoft Translation API,
Translated MyMemory API, LibreTranslate, and DeepL's free and pro APIs


Why Should I Use This?
----------------------

The biggest reason to use translate is to  make translations in a simple way without the need of bigger
effort and can be used as a translation tool like command line



Installation
------------

.. code-block:: bash

   $ pip install translate

Or, you can download the source and

.. code-block:: bash

   $ python setup.py install

Prefix 'sudo' if you encounter a problem.


Features
--------

- Translate your output in real time
- Do translation in your terminal using the command line

Usage
-----

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

      Python command line tool to make online translations

      Example:

           $ translate-cli -t zh the book is on the table
           碗是在桌子上。

      Available languages:

           https://en.wikipedia.org/wiki/ISO_639-1
           Examples: (e.g. en, ja, ko, pt, zh, zh-TW, ...)

    Options:
      --version                 Show the version and exit.
      --generate-config-file    Generate the config file using a Wizard and exit.
      -f, --from TEXT           Sets the language of the text being translated.
                                The default value is 'autodetect'.
      -t, --to TEXT             Set the language you want to translate.
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

The cfg is not for use as a Python module.

or run the command line and follow the steps:

.. code-block:: bash

    $ translate-cli --generate-config-file
    Translate from [autodetect]:
    Translate to: <language you want to translate>
    Provider [mymemory]:
    Secret Access Key []:


Use As A Python Module
----------------------

.. code-block:: python

   In [1]: from translate import Translator
   In [2]: translator= Translator(to_lang="zh")
   In [3]: translation = translator.translate("This is a pen.")
   Out [3]: 这是一支笔

The result is usually a unicode string.


Use a different translation provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    In [1]: from translate import Translator
    In [2]: to_lang = 'zh'
    In [3]: secret = '<your secret from Microsoft or DeepL>'
    In [4]: translator = Translator(provider='<the name of the provider, eg. microsoft or deepl>', to_lang=to_lang, secret_access_key=secret)
    In [5]: translator.translate('the book is on the table')
    Out [5]: '碗是在桌子上。'

The DeepL Provider
~~~~~~~~~~~~~~~~~~
To use DeepL's pro API, pass an additional parameter called pro to the Translator object and set it to True and use your pro authentication key as the secret_access_key

.. code-block:: python

    In: translator = Translator(provider='microsoft', to_lang=to_lang, secret_access_key=secret, pro=True)

Documentation
-------------

Check out the latest ``translate`` documentation at `Read the Docs <http://translate-python.readthedocs.io/en/latest/>`_


Contributing
------------

Please send pull requests, very much appreciated.


1. Fork the `repository <https://github.com/terryyin/translate-python>`_ on GitHub.
2. Make a branch off of master and commit your changes to it.
3. Install requirements. ``pip install -r requirements-dev.txt``
4. Install pre-commit. ``pre-commit install``
5. Run the tests with ``py.test -vv -s``
6. Create a Pull Request with your contribution



.. |Docs| image:: https://readthedocs.org/projects/translate-python/badge/?version=latest
   :target: http://translate-python.readthedocs.org/en/latest/?badge=latest
.. |Travis Build Status| image:: https://api.travis-ci.org/terryyin/translate-python.png?branch=master
   :target: https://travis-ci.org/terryyin/translate-python
.. |PyPI Version| image:: https://img.shields.io/pypi/pyversions/translate.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/translate
.. |PyPI License| image:: https://img.shields.io/pypi/l/translate.svg?maxAge=2592000
   :target: https://github.com/terryyin/translate-python/blob/master/LICENSE
.. |PyPI latest| image:: https://img.shields.io/pypi/v/translate.svg?maxAge=360
   :target: https://pypi.python.org/pypi/translate
