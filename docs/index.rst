..
    SATComum documentation master file
    Created by sphinx-quickstart on Wed Jun 24 19:12:11 2015.

Projeto SATComum
================

Este projeto mantém o código comum aos projetos relacionados ao `SAT-CF-e`_,
tais como validadores, formatadores, constantes e utilitários que são usados
nos projetos relacionados.

Nesta documentação você encontrará basicamente a documentação da API para esse
código comum. Para uma visão mais abrangente da tecnologia `SAT-CF-e`_ e de
como estes projetos se relacionam conheça os projetos relacionados.


Projetos Relacionados
---------------------

Este projeto é apenas uma parte de um total de cinco projetos que compõem uma
solução compreensível para a tecnologia SAT-CF-e em linguagem Python,
disponíveis para integração nas aplicações de ponto-de-venda. São eles:

* Projeto `SATCFe`_
    Abstração para acesso às funções da biblioteca SAT em Python. Visite a
    `documentação desse projeto <https://satcfe.readthedocs.io/>`_ para uma
    visão mais abrangente da tecnologia `SAT-CF-e`_ e de como estes projetos
    se relacionam.

* Projeto `SATExtrato`_
    Impressão dos extratos do CF-e-SAT. Este projeto é capaz de imprimir
    extratos de documentos de venda ou de cancelamento diretamente a partir dos
    documentos XML que os representam. A impressão tem um alto grau de
    compatibilidade com mini-impressoras (conhecidas como impressoras
    não-fiscais) já que é baseada na tecnologia Epson |reg| ESC/POS |trade|
    através do projeto `PyESCPOS`_.

* Projeto `SATHub`_
    Torna possível o compartilhamento de equipamentos SAT com múltiplos pontos-
    de-venda, além de tornar possível que aplicações heterogêneas, escritas em
    outras linguagens de programação ou de outras plataformas, acessem o
    equipamento SAT.

* Projeto `PyESCPOS`_
    Implementa o suporte à tecnologia Epson |reg| ESC/POS |trade| compatível
    com a imensa maioria das mini-impressoras disponíveis no mercado.


Participe
---------

Participe deste projeto ou de qualquer um dos projetos relacionados. Se você
puder contribuir com código, excelente! Faça um clone do repositório,
modifique o que acha que deve e faça o *pull-request*. Teremos
`prazer <https://www.python.org/dev/peps/pep-0008/>`_ em
`aceitar <http://docs.python-guide.org/en/latest/writing/style/>`_ o seu
`código <https://intermediate-and-advanced-software-carpentry.readthedocs.io>`_.

Se você não quer (ou não pode) programar, também pode contribuir com
documentação. Ou ainda, se você vir algo errado ou achar que algo não está
certo, `conte pra gente <https://github.com/base4sistemas/satcomum/issues>`_
criando um incidente na página do projeto.

Siga-nos no `Github <https://github.com/base4sistemas>`_ ou no
`Twitter <https://twitter.com/base4sistemas>`_.


Documentação da API
===================

.. toctree::
    :maxdepth: 2

    apidoc/br
    apidoc/constantes
    apidoc/ersat
    apidoc/util


Tabelas e Índices
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. include:: references.rst
