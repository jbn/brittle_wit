.. image:: https://travis-ci.org/jbn/brittle_wit.svg?branch=master
    :target: https://travis-ci.org/jbn/brittle_wit
.. image:: https://ci.appveyor.com/api/projects/status/69kj3prrrieyp8q2/branch/master?svg=true
    :target: https://ci.appveyor.com/project/jbn/brittle_wit/branch/master 
.. image:: https://coveralls.io/repos/github/jbn/brittle_wit/badge.svg?branch=master
    :target: https://coveralls.io/github/jbn/brittle_wit?branch=master 
.. image:: https://img.shields.io/pypi/dm/brittle_wit.svg
    :target: https://pypi.python.org/pypi/brittle_wit
.. image:: https://img.shields.io/pypi/v/brittle_wit.svg
    :target: https://pypi.python.org/pypi/brittle_wit
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://raw.githubusercontent.com/jbn/brittle_wit/master/LICENSE
.. image:: https://img.shields.io/pypi/pyversions/brittle_wit.svg
    :target: https://pypi.python.org/pypi/brittle_wit

About
=====

**Brittle Wit is a Twitter Lib for Python.**

-  It uses `asyncio <https://docs.python.org/3/library/asyncio.html>`__,
   `aiohttp <http://aiohttp.readthedocs.org/en/stable/>`__, and Python
   3.5+ (async/await).
-  It is rigorously polite in its adherence to `Twitter's rate
   limits <https://dev.twitter.com/rest/public/rate-limiting>`__.
-  It scales well.
-  It works as a library or a server.

Warning
-------

I started developing this package months ago. I wanted to create some
tools for for media company agenda management. But, I ran out of
safety-net cash, and had to go back to a 9–5 (on top of my Ph.D. work).
Consequently, this library is unfinished and certainly buggy. I'm
releasing it earlier than I'd prefer as a mean of facilitating
replicability for a post I wrote on Medium.

Developer, beware.

Installation
------------

From a Python 3.5 environment,

.. code:: bash

    pip install brittle_wit
