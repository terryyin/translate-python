google-translate-python
=======================

Google translate as Python module &amp; command line tool. No key, no authentication whatsoever. The default target language is Simplified Chinese.

利用google translate实现的命令行工具（translate），也可以当做Python模块用在你的代码中。

## Installation

<pre>
pip install translate
</pre> 

Or, you can download the source and

<pre>
python setup.py install
</pre> 

Add sudo in the beginning if you met problem.

## Command-Line Usage

In your command-line:

<pre>
translate "This is a pen."
</pre>

Or

<pre>
translate -f zh -t ja 我是谁？
</pre>

## Use As A Python Module

<pre>
from translate import Translator
translator= Translator(to_lang="zh")
translation = translator.translate("This is a pen.")
</pre>

The result is in translation, and it's usually a unicode string.
