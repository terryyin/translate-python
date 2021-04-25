#!/usr/bin/env python
# encoding: utf-8

from .mymemory_translated import MyMemoryProvider  # noqa
from .microsoft import MicrosoftProvider  # noqa
from .deepl import DeeplProvider  # noqa

__all__ = ['MyMemoryProvider', 'MicrosoftProvider', 'DeeplProvider']
