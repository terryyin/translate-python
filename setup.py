#!/usr/bin/env python
# encoding: utf-8
import codecs
import os
import re
from setuptools import setup, Command


here = os.path.abspath(os.path.dirname(__file__))
version = '0.0.0'
description = (
    'This is a simple, yet powerful command line translator with google translate behind it. '
    'You can also use it as a Python module in your code.'
)
changes = os.path.join(here, "CHANGES.rst")
pattern = r'^(?P<version>[0-9]+.[0-9]+(.[0-9]+)?)'
with codecs.open(changes, encoding='utf-8') as changes:
    for line in changes:
        match = re.match(pattern, line)
        if match:
            version = match.group("version")
            break


class VersionCommand(Command):
    description = 'Show library version'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print(version)

with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n{}'.format(f.read())

with codecs.open(os.path.join(here, 'CHANGES.rst'), encoding='utf-8') as f:
    changes = f.read()
    long_description += '\n\nChangelog:\n----------\n\n{}'.format(changes)


# Requirements
install_requirements = ['requests>=2.18.4']

setup(
    name='translate',
    version=version,
    description=description,
    long_description=long_description,
    url='https://github.com/terryyin/google-translate-python',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'License :: Freeware',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Education',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
        'Programming Language :: Python :: 3.5'
        'Programming Language :: Python :: 3.6'
    ],
    py_modules=['translate'],
    author='Terry Yin',
    author_email='terry.yinze@gmail.com',
    install_requires=install_requirements,
    scripts=['translate'],
    cmdclass={'version': VersionCommand},
)
