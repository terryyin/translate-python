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
from .version import __version__


TRANSLATION_FROM_DEFAULT = 'autodetect'
CONFIG_FILE_PATH = '~/.python-translate.cfg'
VERSION_FILE = 'VERSION.txt'

here = os.path.dirname(os.path.abspath(__file__))


def get_config_info(lang_type):
    config_file_path = os.path.expanduser(CONFIG_FILE_PATH)
    lang_types = ('from_lang', 'to_lang')
    if not os.path.exists(config_file_path) or lang_type not in lang_types:
        return ''

    config_parser = ConfigParser()
    config_parser.read(config_file_path)
    default_section = 'DEFAULT'
    return config_parser.get(default_section, lang_type)


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    click.echo('translate, version {}'.format(__version__))
    ctx.exit()


@click.command()
@click.option(
    '--version', is_flag=True, callback=print_version,
    expose_value=False,
    is_eager=True,
    help='Show the version and exit.'
)
@click.option(
    'from_lang', '--from', '-f',
    default=get_config_info('from_lang') or TRANSLATION_FROM_DEFAULT,
    help="Language of the text being translated. The default value is 'autodetect'"
)
@click.option(
    'to_lang', '--to', '-t',
    default=get_config_info('to_lang'),
    prompt='Translate to',
    help='Language you want translate.'
)
@click.argument('text', nargs=-1, type=click.STRING, required=True)
def main(from_lang, to_lang, text):
    """
    Python command line tool to make on line translations

    Example: \n
    \b
    \t $ translate-cli -t zh the book is on the table
    \t 碗是在桌子上。

    Available languages: \n
    \b
    \t https://en.wikipedia.org/wiki/ISO_639-1
    \t Examples: (e.g. en, ja, ko, pt, zh, zh-TW, ...)
    """
    text = ' '.join(text)
    translator = Translator(from_lang=from_lang, to_lang=to_lang)

    translation = translator.translate(text)
    if sys.version_info.major == 2:
        translation = translation.encode(locale.getpreferredencoding())

    click.echo(translation)

    return translation
