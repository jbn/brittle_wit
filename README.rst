.. image:: https://travis-ci.org/jbn/brittle_wit.svg?branch=master
    :target: https://travis-ci.org/jbn/brittle_wit
.. image:: https://ci.appveyor.com/api/projects/status/9k78nhy88v51fd69?svg=true
    :target: https://ci.appveyor.com/project/jbn/brittle-wit/branch/master
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

-------------------------------------------------------------------------------

====================
What is Brittle Wit?
====================

**Brittle Wit is a Twitter Lib for Python.**

-  It uses `asyncio <https://docs.python.org/3/library/asyncio.html>`__,
   `aiohttp <http://aiohttp.readthedocs.org/en/stable/>`__, and Python
   3.5+ (async/await).
-  It is rigorously polite in its adherence to `Twitter's rate
   limits <https://dev.twitter.com/rest/public/rate-limiting>`__.
-  It scales well.
-  It works as a library or a server.
-  "Namespaces are one honking great idea -- let's do more of those!"


--------------
A Trivial Demo
--------------

This code is explained thoroughly in the documentation. It fetches jacks first
tweet.

.. code-block:: python
      
    import brittle_wit as bw
    from brittle_wit.executors import debug_blocking_request
    from brittle_wit import rest_api


    APP_CRED = bw.AppCredentials.load_from_env()
    CLIENT_CRED = bw.ClientCredentials.load_from_env()
    req = rest_api.statuses.lookup(id=20)
    resp = debug_blocking_request(APP_CRED, CLIENT_CRED, req)
    jacks_first_tweet = resp.json()

    print(jacks_first_tweet)

