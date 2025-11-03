#!/usr/bin/env python
# encoding: utf-8

from .mymemory_translated import MyMemoryProvider  # noqa
from .microsoft import MicrosoftProvider  # noqa
from .deepl import DeeplProvider  # noqa
from .libre import LibreProvider
from .yandex import YandexProvider

__all__ = ['MyMemoryProvider', 'MicrosoftProvider', 'DeeplProvider', 'LibreProvider', 'YandexProvider']
