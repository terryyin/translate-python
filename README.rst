========================
Translate Tool in Python
========================

.. image:: https://api.travis-ci.org/terryyin/google-translate-python.png?branch=master
    :target: https://travis-ci.org/terryyin/google-translate-python
.. image:: https://badge.fury.io/py/translate.svg
    :target: https://badge.fury.io/py/translate

Translate is a simple but powerful translation tool written in python with with support for
multiple translation providers. By now we are integrated with Microsoft Translation API and
Translated MyMemory API


Why Should I Use This?
----------------------

The biggest reason to use translate is make translations in a simple way without the need of much
effort and can be used as a translation tool like command line


Installation
------------

.. code-block:: bash

   $ pip install translate

Or, you can download the source and

.. code-block:: bash

   $ python setup.py install

Add sudo in the beginning if you met problem.


Features
--------

 - Translate your outputs in real time
 - Do translation in your terminal using command line

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


Documentation
~~~~~~~~~~~~~

Check out the latest ``translate`` documentation at `Read the Docs` website. (In contruction)


Contributing
------------

Please send pull requests, very much appriciated.


1. Fork the `repository <https://github.com/terryyin/translate-python>`_ on GitHub.
2. Make a branch off of master and commit your changes to it.
3. Install requirements. ``pip install -r requirements-dev.txt``
4. Install pre-commit. ``pre-commit install``
5. Run the tests with ``py.test -vv -s``
6. Create a Pull Request with your contribution
