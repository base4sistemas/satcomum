# -*- coding: utf-8 -*-
#
# setup.py
#
# Copyright 2015 Base4 Sistemas Ltda ME
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import absolute_import
from __future__ import unicode_literals

import io
import os
import re

from setuptools import setup


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


def read_version():
    content = read(os.path.join('satcomum', '__init__.py'))
    return re.search(r"__version__ = '([^']+)'", content).group(1)


long_description = read('README.rst')


setup(
        name='satcomum',
        version=read_version(),
        description='Código comum à implementação do SAT-CF-e.',
        long_description=long_description,
        long_description_content_type='text/x-rst',
        packages=[
                'satcomum',
            ],
        install_requires=[
                'future',
                'six',
            ],
        include_package_data=True,
        license='Apache Software License',
        platforms='any',
        url='https://github.com/base4sistemas/satcomum',
        author='Daniel Gonçalves',
        author_email='daniel@base4.com.br',
        classifiers=[
                'Development Status :: 5 - Production/Stable',
                'Environment :: Other Environment',
                'Intended Audience :: Developers',
                'Intended Audience :: Information Technology',
                'License :: OSI Approved :: Apache Software License',
                'Natural Language :: Portuguese (Brazilian)',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Programming Language :: Python :: 2.7',
                'Programming Language :: Python :: 3.6',
                'Programming Language :: Python :: 3.7',
                'Programming Language :: Python :: 3.8',
                'Programming Language :: Python :: 3.9',
                'Topic :: Office/Business :: Financial :: Point-Of-Sale',
                'Topic :: Software Development :: Libraries :: Python Modules',
                'Topic :: Utilities',
            ]
    )
