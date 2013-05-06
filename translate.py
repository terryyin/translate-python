import urllib2
import re

class Translator:
    pattern = re.compile(r"\[\[\[\"([^\"]*)\"")
    def __init__(self, to_lang):
        self.to_lang = to_lang
   
    def translate(self, source):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.168 Safari/535.19'}
        
        request = urllib2.Request(url="http://translate.google.com/translate_a/t?client=t&ie=UTF-8&oe=UTF-8&sl=en&tl=%s&text=%s" % (self.to_lang, source), headers = headers)
        r = urllib2.urlopen(request)
        result =self.pattern.match(r.read())
        return result.group(1)

