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
from .constants import CONFIG_FILE_PATH, DEFAULT_PROVIDER, TRANSLATION_FROM_DEFAULT


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
    '--version',
    callback=print_version,
    expose_value=False,
    is_flag=True,
    is_eager=True,
    help='Show the version and exit.'
)
@click.option(
    'from_lang', '--from', '-f',
    default=get_config_info('from_lang') or TRANSLATION_FROM_DEFAULT,
    help="Sets the language of the text being translated. The default value is 'autodetect'"
)
@click.option(
    'to_lang', '--to', '-t',
    default=get_config_info('to_lang'),
    prompt='Translate to',
    help='Sets the language you want to translate.'
)
@click.option(
    'provider', '--provider', '-p',
    default=DEFAULT_PROVIDER,
    help="The providers name you wish to use. The default value is '{}'".format(DEFAULT_PROVIDER)
)
@click.option(
    'secret_access_key', '--secret_access_key',
    help="Set the secret access key used to get provider oAuth token",
    required=False,
)
@click.argument('text', nargs=-1, type=click.STRING, required=True)
def main(from_lang, to_lang, provider, secret_access_key, text):
    """
    Python command line tool to make on line translations

    \b
    Example:

    \t $ translate-cli -t zh the book is on the table
    \t 碗是在桌子上。

    \b
    Available languages:

    \t https://en.wikipedia.org/wiki/ISO_639-1
    \t Examples: (e.g. en, ja, ko, pt, zh, zh-TW, ...)
    """
    text = ' '.join(text)

    kwargs = dict(from_lang=from_lang, to_lang=to_lang, provider=provider)
    if provider != DEFAULT_PROVIDER:
        kwargs['secret_access_key'] = secret_access_key

    translator = Translator(**kwargs)
    translation = translator.translate(text)
    if sys.version_info.major == 2:
        translation = translation.encode(locale.getpreferredencoding())

    click.echo(translation)

    return translation
