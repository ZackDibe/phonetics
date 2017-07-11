===========
 Phonetics
===========

|PyPI-Status|  |PyPI-Versions|

|LICENCE|

The phonetics module computes the phonetic key of a string using different algorithms.

 * Soundex
 * NYSISS
 * Metaphone
 * Double Metaphone

------------------------------------------

.. contents:: Table of contents
   :backlinks: top
   :local:


Installation
============

Latest PyPI stable release
--------------------------

|PyPI-Status|

.. code:: sh

    pip install phonetics

Latest development release on github
------------------------------------

|GitHub-Status| |GitHub-Stars| |GitHub-Forks|

Pull and install in the current directory:

.. code:: sh

    pip install -e git+https://github.com/Zack--/phonetics.git@master#egg=phonetics

Running tests
-------------

By `Duncan McGreggor <https://github.com/oubiwann>`_

.. code-block:: shell

    $ python -m unittest discover phonetics/tests/ -v

Or

.. code:: sh

   nosetests --with-coverage --cover-package=phonetics

Usage
=====

.. code-block:: python

    >>> import phonetics
    >>> phonetics.dmetaphone('Danger')
    ('TNJR', 'TNKR')


Module Contents
===============

The ``phonetics`` module defines the following function:

``phonetics``. **soundex**\(*source* [, *size=4*])
  Use the soundex algorithm to create the phonetic key of the **source** string.

``phonetics``. **nysiis**\(*source*)
  Use the New York State Identification and Intelligence System to create the phonetic key of the **source** string.

``phonetics``. **metaphone**\(*source*)
 |  Use the metaphone algorithm to create the phonetic key of the **source** string.
 |  Based on `Lawrence Philips' Metaphone Algorithm <http://aspell.net/metaphone/>`__.

``phonetics``. **dmetaphone**\(*source*)
 |  Use the double methaphone algorithm to create the phonetic key of the **source** string.
 |  Based on `Lawrence Philips' Metaphone Algorithm <http://aspell.net/metaphone/>`__.

Contributions
=============

All source code is hosted on `GitHub <https://github.com/ToasterCo/apiaiassistant>`__.
Contributions are welcome.

See the
`CONTRIBUTING <https://raw.githubusercontent.com/Zack--/apiaiassistant/master/CONTRIBUTING.md>`__
file for more information.


LICENCE
=======

Open Source : |LICENCE|

Authors
=======

Ranked by contributions.

-  Zack Dibe (Zack--) *

`*` Original author

.. |PyPI-Status| image:: https://img.shields.io/pypi/v/phonetics.svg
   :target: https://pypi.python.org/pypi/phonetics

.. |PyPI-Downloads| image:: https://img.shields.io/pypi/dm/phonetics.svg
   :target: https://pypi.python.org/pypi/phonetics

.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/phonetics.svg
   :target: https://pypi.python.org/pypi/phonetics

.. |LICENCE| image:: https://img.shields.io/pypi/l/phonetics.svg
   :target: https://raw.githubusercontent.com/Zack--/phonetics/master/LICENCE

.. |GitHub-Status| image:: https://img.shields.io/github/tag/Zack--/phonetics.svg?maxAge=2592000
   :target: https://github.com/Zack--/phonetics/releases

.. |GitHub-Forks| image:: https://img.shields.io/github/forks/Zack--/phonetics.svg
   :target: https://github.com/Zack--/phonetics/network

.. |GitHub-Stars| image:: https://img.shields.io/github/stars/Zack--/phonetics.svg
   :target: https://github.com/Zack--/phonetics/stargazers
