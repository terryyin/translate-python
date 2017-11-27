#!/usr/bin/env python
# encoding: utf-8
import codecs
import os
import re
from setuptools import find_packages, setup, Command


here = os.path.dirname(os.path.abspath(__file__))
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


# Save last Version
def save_version():
    version_path = os.path.join(here, "translate/version.py")

    with open(version_path) as version_file_read:
        content_file = version_file_read.read()

    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    mo = re.search(VSRE, content_file, re.M)
    current_version = mo.group(1)

    content_file = content_file.replace(current_version, "{}".format(version))

    with open(version_path, 'w') as version_file_write:
        version_file_write.write(content_file)


save_version()


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
with codecs.open(os.path.join(here, 'README.rst')) as f:
    long_description = '\n{}'.format(f.read())

# Get change log
with codecs.open(os.path.join(here, 'CHANGES.rst')) as f:
    changelog = f.read()
    long_description += '\n\n{}'.format(changelog)

# Requirements
with codecs.open(os.path.join(here, 'requirements.txt')) as f:
    install_requirements = [line.split('#')[0].strip() for line in f.readlines() if not line.startswith('#')]

with codecs.open(os.path.join(here, 'requirements-dev.txt')) as f:
    tests_requirements = [line.replace('\n', '') for line in f.readlines() if not line == '-r requirements.txt\n']


setup(
    author='Terry Yin',
    author_email='terry.yinze@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python',
        'Topic :: Education',
    ],
    cmdclass={'version': VersionCommand},
    description=description,
    entry_points='''
        [console_scripts]
        translate-cli=translate.__main__:cli
    ''',
    install_requires=install_requirements,
    keywords='translate translation command line',
    license='MIT',
    long_description=long_description,
    name='translate',
    packages=find_packages(exclude=['docs', 'tests', 'tests.*', 'requirements']),
    setup_requires=['pytest-runner'],
    tests_require=tests_requirements,
    url='https://github.com/terryyin/google-translate-python',
    version=version,
)
