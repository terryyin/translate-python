try:
    import urllib2 as request
except:
    from urllib import request

import re

class Translator:
    pattern = re.compile(r"\[\[\[\"([^\"]*)\"")
    def __init__(self, to_lang):
        self.to_lang = to_lang
   
    def translate(self, source):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.168 Safari/535.19'}
        
        req = request.Request(url="http://translate.google.com/translate_a/t?client=t&ie=UTF-8&oe=UTF-8&sl=en&tl=%s&text=%s" % (self.to_lang, source), headers = headers)
        r = request.urlopen(req)
        result =self.pattern.match(r.read().decode('utf-8'))
        return result.group(1)

