
.. image:: https://img.shields.io/pypi/v/satcomum.svg
    :target: https://pypi.python.org/pypi/satcomum/
    :alt: Latest version

.. image:: https://img.shields.io/pypi/pyversions/satcomum.svg
    :target: https://pypi.python.org/pypi/satcomum/
    :alt: Supported Python versions

.. image:: https://img.shields.io/pypi/status/satcomum.svg
    :target: https://pypi.python.org/pypi/satcomum/
    :alt: Development status

.. image:: https://readthedocs.org/projects/satcomum/badge/?version=latest
    :target: https://satcomum.readthedocs.io/pt_BR/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/pypi/l/satcomum.svg
    :target: https://pypi.python.org/pypi/satcomum/
    :alt: License

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/base4sistemas/satcfe
   :target: https://gitter.im/base4sistemas/satcfe?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge


Código Comum ao SAT-CF-e
========================


    This project holds common code for projects related to `SAT-CF-e`_
    which is a system for autorization and transmission of fiscal documents,
    developed by Finance Secretary of state of São Paulo, Brazil. The entire
    project, including variables, methods and class names, as well as
    documentation, are written in brazilian portuguese.

    Head over to `SAT-CF-e`_ official website for more information (in
    brazilian portuguese only).


Este projeto mantém o código comum aos projetos relacionados ao `SAT-CF-e`_,
tais como validadores, formatadores, constantes e utilitários que são usados
nos projetos relacionados:

* Abstração do acesso ao equipamento SAT, `Projeto SATCFe`_
* Impressão dos extratos do CF-e-SAT, `Projeto SATExtrato`_
* Compartilhamento de Equipamentos SAT via RESTful API, `Projeto SATHub`_


Desenvolvimento e Testes
========================

Configure o ambiente de desenvolvimento e execute os testes:

.. sourcecode:: shell

    $ git clone https://github.com/base4sistemas/satcomum.git
    $ cd satcomum
    $ python -m venv .env
    $ source .env/bin/activate
    (.env) $ pip install --upgrade pip
    (.env) $ pip install -r requirements/dev.txt
    (.env) $ tox


.. _`SAT-CF-e`: https://portal.fazenda.sp.gov.br/servicos/sat/
.. _`Projeto SATCFe`: https://github.com/base4sistemas/satcfe
.. _`Projeto SATExtrato`: https://github.com/base4sistemas/satextrato
.. _`Projeto SATHub`: https://github.com/base4sistemas/sathub
