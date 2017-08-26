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

.. code:: python

    from brittle_wit.app import load_app_cred, load_single_user_cred, App
    import brittle_wit.patterns as ptns 

    # Reads ENV variables: 
    # - TWITTER_APP_KEY
    # - TWITTER_APP_SECRET
    APP_CRED = load_app_cred()

    # Reads ENV variables: 
    # - TWITTER_USER_ID
    # - TWITTER_USER_TOKEN
    # - TWITTER_USER_SECRET
    CLIENT_CRED = load_single_user_cred()

    with App.reactor(APP_CRED) as app:
        ctx = app.client_context(CLIENT_CRED)
        followers_of = app.run_until_complete(ptns.collect_follower_ids_for(ctx, 'generativist'))
        followers_infos = app.run_until_complete(ptns.collect_user_infos_by_ids(ctx, followers_of))
