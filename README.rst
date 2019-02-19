
Código Comum ao SAT-CF-e
========================

.. image:: https://img.shields.io/pypi/status/satcomum.svg
    :target: https://pypi.python.org/pypi/satcomum/
    :alt: Development status

.. image:: https://img.shields.io/pypi/v/satcomum.svg
    :target: https://pypi.python.org/pypi/satcomum/
    :alt: PyPI - Latest version

.. image:: https://img.shields.io/pypi/pyversions/satcomum.svg
    :target: https://pypi.python.org/pypi/satcomum/
    :alt: PyPI - Python version

.. image:: https://img.shields.io/pypi/l/satcomum.svg
    :target: https://pypi.python.org/pypi/satcomum/
    :alt: PyPI - License

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :target: https://gitter.im/base4sistemas/satcfe?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
   :alt: Join chat on Gitter

----

    This project holds the common code for projects related to `SAT-CF-e`_
    which is a system for autorization and transmission of fiscal documents,
    developed by Finance Secretary of state of São Paulo, Brazil. This entire
    project, variables, methods and class names, as well as documentation, are
    written in brazilian portuguese.

    Refer to the
    `oficial web site <https://portal.fazenda.sp.gov.br/servicos/sat/>`_ for
    more information (in brazilian portuguese only).

----

.. image:: https://travis-ci.org/base4sistemas/satcomum.svg?branch=master
    :target: https://travis-ci.org/base4sistemas/satcomum
    :alt: Travis-CI - Build status

.. image:: https://img.shields.io/badge/docs-latest-green.svg
    :target: http://satcfe.readthedocs.org/
    :alt: Latest documentation

Este projeto mantém o código comum aos projetos relacionados ao `SAT-CF-e`_,
tais como validadores, formatadores, constantes e utilitários que são usados
nos projetos relacionados:

* Abstração do acesso ao equipamento SAT, `Projeto SATCFe`_
* Impressão dos extratos do CF-e-SAT, `Projeto SATExtrato`_
* Compartilhamento de Equipamentos SAT via RESTful API, `Projeto SATHub`_


Desenvolvimento e Testes
========================

Para executar testes locais em todas as versões suportadas do Python:

.. sourcecode:: shell

    $ git clone git@github.com:base4sistemas/satcomum.git
    $ cd satcomum
    $ pipenv install --dev --clear
    $ pipenv run tox


.. _`SAT-CF-e`: https://portal.fazenda.sp.gov.br/servicos/sat/
.. _`Projeto SATCFe`: https://github.com/base4sistemas/satcfe
.. _`Projeto SATExtrato`: https://github.com/base4sistemas/satextrato
.. _`Projeto SATHub`: https://github.com/base4sistemas/sathub
