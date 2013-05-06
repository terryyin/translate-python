#!/usr/bin/env python
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <terry.yinzhe@gmail.com> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return to Terry Yin.
#
# The idea of this is borrowed from <mort.yao@gmail.com>'s brilliant work
#    https://github.com/soimort/google-translate-cli
# He uses "THE BEER-WARE LICENSE". That's why I use it too. So you can buy him a 
# beer too.
# ----------------------------------------------------------------------------
import re
try:
    import urllib2 as request
    from urllib import quote
except:
    from urllib import request
    from urllib.parse import quote

class Translator:

    pattern = re.compile(r"\[\[\[\"(([^\"\\]|\\.)*)\"")

    def __init__(self, to_lang):
        self.to_lang = to_lang
   
    def translate(self, source):
        escaped_source = quote(source, '')
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.168 Safari/535.19'}
        req = request.Request(url="http://translate.google.com/translate_a/t?client=t&ie=UTF-8&oe=UTF-8&sl=en&tl=%s&text=%s" % (self.to_lang, escaped_source), headers = headers)
        r = request.urlopen(req)
        result =self.pattern.match(r.read().decode('utf-8'))
        return self.unescape(result.group(1))

    def unescape(self, text):
        return re.sub(r"\\.?", lambda x:eval('"%s"'%x.group(0)), text)
