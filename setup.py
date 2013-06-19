#!/usr/bin/env python
# coding=utf-8

__author__ = 'Esteban Garcia-Gurtubay'
__copyright__ = 'Ericsson Spain 2013'
__version__ = 'R13A01'
__email__ = 'esteban.garcia.gurtubay@gmail.com'
__date__ = '19/06/2013 17:07:15'


#from distutils.core import setup               # To make a pip .tar.gz
from setuptools import setup, find_packages     # To make an easy_install .egg

setup(
    name='pysiu',
    version = __version__,
    license='LICENSE.txt',
    author=__author__,
    author_email=__email__,
    description='Python utility libraries for the Ericsson SIU nodes',
    #packages=find_packages(exclude=['other', '*.test']),
    packages=find_packages(exclude=['other',]),
    package_data={'pysiu': ['*.sh'],
                },
)
