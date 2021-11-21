# -*- coding: utf-8 -*-
#
# tests/test_constantes.py
#
# Copyright 2021 Base4 Sistemas
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

from satcomum.constantes import VERSAO_ER
from satcomum.constantes import VERSAO_LAYOUT_ARQUIVO_DADOS_AC


def test_versao_er_sat():
    """Garante correção na versão da ER SAT."""
    assert '2.28.05' == VERSAO_ER


def test_versao_layout_arquivo_dados_ac():
    """Garante correção na versão do Layout do CF-e gerado pela AC."""
    assert '0.07' == VERSAO_LAYOUT_ARQUIVO_DADOS_AC
