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


def get_config_info(option):
    config_file_path = os.path.expanduser(CONFIG_FILE_PATH)
    options = ('from_lang', 'to_lang', 'provider', 'secret_access_key')
    if not os.path.exists(config_file_path) or option not in options:
        return ''

    config_parser = ConfigParser()
    config_parser.read(config_file_path)
    default_section = 'DEFAULT'
    return config_parser.get(default_section, option)


def generate_config(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    config_file_path = os.path.expanduser(CONFIG_FILE_PATH)
    if os.path.exists(config_file_path):
        click.echo('The config already generated.')
        ctx.exit()

    ctx.invoke(config_file({}))
    click.echo('The config file was generated in {}'.format(CONFIG_FILE_PATH))
    ctx.exit()


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    click.echo('translate, version {}'.format(__version__))
    ctx.exit()


@click.command()
@click.option(
    'from_lang', '-f',
    default=TRANSLATION_FROM_DEFAULT,
    prompt='Translate from',
)
@click.option(
    'to_lang', '-t',
    prompt='Translate to',
)
@click.option(
    'provider', '-p',
    default=DEFAULT_PROVIDER,
    prompt='Provider',
)
@click.option(
    'secret_access_key', '-s',
    default="",
    prompt='Secret Access Key',
    required=False
)
@click.pass_context
def config_file(ctx, from_lang, to_lang, provider, secret_access_key):
    config_content = (
        '[DEFAULT]\n'
        'from_lang = {}\n'
        'to_lang = {}\n'
        'provider = {}\n'
        'secret_access_key = {}\n'
    )
    content = config_content.format(from_lang, to_lang, provider, secret_access_key)
    config_file_path = os.path.expanduser(CONFIG_FILE_PATH)
    with open(config_file_path, 'w') as config_file:
        config_file.write(content)


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
    '--generate-config-file',
    callback=generate_config,
    expose_value=False,
    is_flag=True,
    is_eager=True,
    help='Generated the config file using a Wizard and exit.'
)
@click.option(
    'from_lang', '--from', '-f',
    default=get_config_info('from_lang') or TRANSLATION_FROM_DEFAULT,
    help="Sets the language of the text being translated. The default value is 'autodetect'."
)
@click.option(
    'to_lang', '--to', '-t',
    default=get_config_info('to_lang'),
    prompt='Translate to',
    help='Sets the language you want to translate.'
)
@click.option(
    'provider', '--provider', '-p',
    default=get_config_info('provider') or DEFAULT_PROVIDER,
    help="Set the provider you want to use. The default value is '{}'.".format(DEFAULT_PROVIDER)
)
@click.option(
    'secret_access_key', '--secret_access_key',
    default=get_config_info('secret_access_key'),
    help="Set the secret access key used to get provider oAuth token.",
    required=False,
)
@click.option(
    'output_only', '--output_only', '-o',
    default=False,
    is_flag=True,
    help="Set to display the translation only.",
    required=False,
)
@click.option(
    'pro', '--pro',
    default=False,
    is_flag=True,
    help="Set to use DeepL's pro API.",
    required=False,
)
@click.argument('text', nargs=-1, type=click.STRING, required=True)
def main(from_lang, to_lang, provider, secret_access_key, output_only, pro, text):
    """
    Python command line tool to make on line translations

    \b
    Example:
    \b
    \t $ translate-cli -t zh the book is on the table
    \t 碗是在桌子上。

    \b
    Available languages:
    \b
    \t https://en.wikipedia.org/wiki/ISO_639-1
    \t Examples: (e.g. en, ja, ko, pt, zh, zh-TW, ...)
    """
    text = ' '.join(text)

    kwargs = dict(from_lang=from_lang, to_lang=to_lang, provider=provider)
    if provider != DEFAULT_PROVIDER:
        kwargs['secret_access_key'] = secret_access_key
        kwargs['pro'] = pro

    translator = Translator(**kwargs)
    translation = translator.translate(text)
    if sys.version_info.major == 2:
        translation = translation.encode(locale.getpreferredencoding())

    if output_only:
        click.echo(translation)
        return translation

    click.echo('\nTranslation: {}'.format(translation))
    click.echo('-' * 25)
    click.echo('Translated by: {}'.format(translator.provider.name))

    return translation
