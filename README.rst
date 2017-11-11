google-translate-python
=======================

Now google has stop providing free translation API. So I have to switch to
http://mymemory.translated.net/, which has a limit for 1000 words/day free
usage. Please let me know if there's any other better free translation API.

The default from language is English (en).
The default to language is Simplified Chinese (zh). Of course, you can specify it
in the parameter or commandline.

利用google
translate实现的命令行工具（translate），也可以当做Python模块用在你的代码中。

Installation
------------

::

   pip install translate

Or, you can download the source and

::

   python setup.py install

Add sudo in the beginning if you met problem.

Command-Line Usage
------------------

In your command-line:

::

   translate-cli "This is a pen."

Or

::

   translate-cli -f zh -t ja 我是谁？

Use As A Python Module
----------------------

::

   from translate import Translator
   translator= Translator(to_lang="zh")
   translation = translator.translate("This is a pen.")

The result is in translation, and it’s usually a unicode string.

Change Default Languages
----------------------

In ~/.python-translate.cfg:

::

   [DEFAULT]
   from_lang = auto
   to_lang = 'de'

The cfg is not for using as a Python module.
The country code, as far as I know, is following https://en.wikipedia.org/wiki/ISO_639-1.

Contribution
-----------------------

Please send pull requests, very much appriciated.

If you find an incorrect translation, one thing you can do is to create an account at http://mymemory.translated.net/ and fix their data.
