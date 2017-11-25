#!/usr/bin/env python
# encoding: utf-8
import os
import click
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

import locale
import sys

from .translate import Translator

TRANSLATION_FROM_DEFAULT = 'en'
TRANSLATION_TO_DEFAULT = 'zh'
CONFIG_FILE_PATH = '~/.python-translate.cfg'


def get_config_info():
    config_file_path = os.path.expanduser(CONFIG_FILE_PATH)

    if not os.path.exists(config_file_path):
        return {
            'from_lang': TRANSLATION_FROM_DEFAULT,
            'to_lang': TRANSLATION_TO_DEFAULT
        }

    config_parser = ConfigParser()
    config_parser.read(config_file_path)
    default_section = 'DEFAULT'
    return {
        'from_lang': config_parser.get(default_section, 'from_lang'),
        'to_lang': config_parser.get(default_section, 'to_lang')
    }


@click.command()
@click.option(
    'from_lang', '--from', '-f',
    # default=TRANSLATION_FROM_DEFAULT,
    help='Language to be translated.'
)
@click.option(
    'to_lang', '--to', '-t',
    # default=TRANSLATION_TO_DEFAULT,
    help='Language to be translated.'
)
@click.argument('text', nargs=-1, type=click.STRING)
def main(from_lang, to_lang, text):
    config_info = get_config_info()
    # if config_info:
    #     not_default_from_condition = from_lang != TRANSLATION_FROM_DEFAULT
    #     from_lang = from_lang if not_default_from_condition else config_info['from_lang']

    #     not_default_to_condition = to_lang != TRANSLATION_FROM_DEFAULT
    #     to_lang = to_lang if not_default_to_condition else config_info['to_lang']
    from_lang = from_lang or config_info['from_lang']
    to_lang = to_lang or config_info['to_lang']

    if not text:
        sys.exit('Type the text to translate')

    text = ' '.join(text)
    translator = Translator(from_lang=from_lang, to_lang=to_lang)

    translation = translator.translate(text)
    if sys.version_info.major == 2:
        translation = translation.encode(locale.getpreferredencoding())

    sys.stdout.write(translation)
    sys.stdout.write("\n")
    return translation
