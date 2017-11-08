#!/usr/bin/env python
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <terry.yinzhe@gmail.com> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return to Terry Yin.
#
# Now google has stop providing free translation API. So I have to switch to
# http://mymemory.translated.net/, which has a limit for 1000 words/day free
# usage.
#
# The original idea of this is borrowed from <mort.yao@gmail.com>'s brilliant work
#    https://github.com/soimort/google-translate-cli
# ----------------------------------------------------------------------------
'''
This is a simple, yet powerful command line translator with google translate
behind it. You can also use it as a Python module in your code.
'''
from textwrap import wrap

import requests


TRANSLATION_API_MAX_LENGHT = 1000


class Translator:
    def __init__(self, to_lang, from_lang='en'):
        self.from_lang = from_lang
        self.to_lang = to_lang
        self.base_url = 'http://mymemory.translated.net/api/get'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19\
                                       (KHTML, like Gecko) Chrome/18.0.1025.168 Safari/535.19'}

    def _get_translation(self, text):
        languages = '{}|{}'.format(self.from_lang, self.to_lang)
        params = {'q': text, 'langpair': languages}
        response = requests.get(self.base_url, params=params, headers=self.headers)
        data = response.json()

        translation = data['responseData']['translatedText']
        if translation:
            return translation
        else:
            matches = data['matches']
            next_best_match = next(match for match in matches)
            return next_best_match['translation']

    def translate(self, text):
        if self.from_lang == self.to_lang:
            return text
        text_list = wrap(text, TRANSLATION_API_MAX_LENGHT, replace_whitespace=False)
        return ' '.join(self._get_translation(text) for text in text_list)


def main(defvals=None):
    import argparse
    import sys
    import locale

    if defvals is None:
        defvals = {'f': 'en', 't': 'zh'}

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('texts', metavar='text', nargs='+',
                        help='a string to translate(use "" when it\'s a sentence)')
    parser.add_argument('-t', '--to', dest='to_lang', type=str, default=defvals['t'],
                        help='To language (e.g. zh, zh-TW, en, ja, ko). Default is '+defvals['t']+'.')
    parser.add_argument('-f', '--from', dest='from_lang', type=str, default=defvals['f'],
                        help='From language (e.g. zh, zh-TW, en, ja, ko). Default is '+defvals['f']+'.')
    args = parser.parse_args()
    translator = Translator(from_lang=args.from_lang, to_lang=args.to_lang)
    for text in args.texts:
        translation = translator.translate(text)
        if sys.version_info.major == 2:
            translation = translation.encode(locale.getpreferredencoding())
        sys.stdout.write(translation)
        sys.stdout.write("\n")

if __name__ == "__main__":
    main()
