#!/usr/bin/env python
# encoding: utf-8
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <terry.yinzhe@gmail.com> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return to Terry Yin.
import argparse
import sys
import locale

from .translate import Translator

TRANSLATION_FROM_DEFAULT = 'en'
TRANSLATION_TO_DEFAULT = 'zh'
HELPER_LANGUAGES = '(e.g. en, ja, ko, pt, zh, zh-TW, ...)'
TRANSLATION_CLIENT = 'translate-cli'
MAIN_FILE = '__main__'


def main(defvals=None):
    if not defvals:
        defvals = {'f': TRANSLATION_FROM_DEFAULT, 't': TRANSLATION_TO_DEFAULT}

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '-t', '--to', dest='to_lang', type=str, default=defvals['t'],
        help='To language {}. Default is {}.'.format(HELPER_LANGUAGES, defvals['t'])
    )
    parser.add_argument(
        '-f', '--from', dest='from_lang', type=str, default=defvals['f'],
        help='From language {}. Default is {}.'.format(HELPER_LANGUAGES, defvals['f'])
    )
    parser.add_argument(
        'texts', metavar='text', nargs='+',
        help='a string to translate(use "" when it\'s a sentence)'
    )

    if TRANSLATION_CLIENT in sys.argv[0] or MAIN_FILE in sys.argv[0]:
        sys.argv.pop(0)

    parsed_args = parser.parse_args(sys.argv)

    translator = Translator(from_lang=parsed_args.from_lang, to_lang=parsed_args.to_lang)
    text = ' '.join(parsed_args.texts)
    translation = translator.translate(text)
    if sys.version_info.major == 2:
        translation = translation.encode(locale.getpreferredencoding())

    sys.stdout.write(translation)
    sys.stdout.write("\n")
    return translation
