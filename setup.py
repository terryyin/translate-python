#!/usr/bin/env python
# encoding: utf-8
import codecs
import os
import re
from setuptools import find_packages, setup, Command


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


# Get the long description
with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Get version
with codecs.open(os.path.join(here, 'CHANGES.rst'), encoding='utf-8') as f:
    changelog = f.read()

# Requirements
with codecs.open(os.path.join(here, 'requirements.txt')) as f:
    install_requirements = [line.split('#')[0].strip() for line in f.readlines() if not line.startswith('#')]

with codecs.open(os.path.join(here, 'requirements-dev.txt')) as f:
    tests_requirements = [line.replace('\n', '') for line in f.readlines() if not line == '-r requirements.txt\n']

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
        'Programming Language :: Python :: 3.5'
    ],
    author='Terry Yin',
    author_email='terry.yinze@gmail.com',
    packages=find_packages(exclude=['docs', 'tests', 'tests.*', 'requirements']),
    setup_requires=['pytest-runner'],
    install_requires=install_requirements,
    tests_require=tests_requirements,
    scripts=['translate-cli'],
    cmdclass={'version': VersionCommand},
)
