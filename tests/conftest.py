# -*- coding: utf-8 -*-
#
# tests/conftest.py
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

import os
import shutil

from builtins import str as text

import pytest


@pytest.fixture(scope='function')
def datadir(tmpdir, request):
    path, _ = os.path.split(request.module.__file__)
    dirname = os.path.join(path, 'data')
    shutil.copytree(dirname, text(tmpdir.join('data')))
    return tmpdir
