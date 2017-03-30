=========
Phonetics
=========

The phonetics module computes the phonetic key of a string using different algorithms.

 * Soundex
 * NYSISS
 * Metaphone
 * Double Metaphone

The phonetics module defines the following function:

phonetics.soundex(source[, size=4])
  Use the soundex algorithm to create the phonetic key of the *source* string.

phonetics.nysiis(source)
  Use the New York State Identification and Intelligence System to create the phonetic key of the *source* string.

phonetics.metaphone(source)
  Use the metaphone algorithm to create the phonetic key of the *source* string.

phonetics.dmetaphone(source)
  Use the double methaphone algorithm to create the phonetic key of the *source* string.


Based on `Lawrence Philips' Metaphone Algorithm <http://aspell.net/metaphone/>`_

Installation
************

.. code-block:: shell

    $ pip install phonetics


Usage
*****

.. code-block:: python

    >>> import phonetics
    >>> phonetics.dmetaphone('Danger')
    ('TNJR', 'TNKR')


Tests
*****

By `Duncan McGreggor <https://github.com/oubiwann>`_

.. code-block:: shell

    $ python -m unittest discover phonetics/tests/ -v
