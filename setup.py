#!/usr/bin/env python
# encoding: utf-8
'''
'''
import translate
from distutils.core import setup


def install():
    try:
        long_description = open("README.rst").read()
    except:
        long_description = translate.__doc__

    install_requirements = ['requests>=2.18.4']

    setup(
        name='translate',
        version="3.0.0",
        description=translate.__doc__,
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
        scripts=['translate']
    )

if __name__ == "__main__":
    install()
