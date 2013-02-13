#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
from setuptools import setup, find_packages

current_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(current_dir, 'README.markdown')) as readme_file:
    with open(os.path.join(current_dir, 'CHANGES.markdown')) as changes_file:
        long_description = readme_file.read() + '\n' + changes_file.read()

setup (
    name = 'qubob',
    version='0.1alfa',
    author='Kamil Warguła @Quamilek',
    author_email = 'kwargula@gmail.com',
    description = "Example usage django-bob library",
    long_description = long_description,
    url = 'https://github.com/quamilek/qubob',
    keywords = '',
    platforms = ['any'],
    license = 'Apache Software License v2.0',
    packages = find_packages('src'),
    include_package_data = True,
    package_dir = {'example':'src'},
    zip_safe = False,
    install_requires = [
        'django==1.4.3',
        'django-bob==1.5.3',
        'django-jquery==1.9.0',
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Software Development :: User Interfaces',
    ]
)
