#!/usr/bin/env python
# encoding: utf-8
'''
'''
import translate
from distutils.core import setup
def install():
    try:
        long_description = open("README.md").read()
    except:
        long_description = translate.__doc__
    setup(
          name = 'translate',
          version = "0.0.3",
          description = translate.__doc__,
          long_description = long_description,
          url = 'https://github.com/terryyin/google-translate-python',
          classifiers = ['Development Status :: 4 - Beta',
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
                     'Programming Language :: Python :: 3.3'],
          py_modules = ['translate'],
          author = 'Terry Yin',
          author_email = 'terry.yinze@gmail.com',
          scripts=['translate']
          )

if __name__ == "__main__":
    install()
