#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'policypools'
DESCRIPTION = 'Provides thread and process pools with policies'
URL = 'https://github.com/alexanderepstein/policypools'
EMAIL = 'alexanderepstein@tuta.io'
AUTHOR = 'Alexander Epstein'
VERSION = '0.0.11'

long_description = "For information on this package refer to the github: %s" % URL
# What packages are required for this module to be executed?
required = []

# Where the magic happens:
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    entry_points={},
    keywords=['multithreading', 'policy', 'thread-pool', 'thread-policypools', 'policies'],  # arbitrary keywords
    install_requires=required,
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
