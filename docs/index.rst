Async -OAuthlib: OAuth for Humans
===================================

Requests-OAuthlib uses the Python
`Aiohttp <https://github.com/aio-libs/aiohttp/>`_ and
`OAuthlib <https://github.com/idan/oauthlib/>`_ libraries to provide an
easy-to-use Python interface for building OAuth1 and OAuth2 clients.


Overview
--------

A simple Flask application which connects to the Github OAuth2 API looks
approximately like this:

.. code-block:: python

    from async_oauthlib import OAuth2Session

    from quart import Quart, request, redirect, session, url_for
    from quart.json import jsonify

    # This information is obtained upon registration of a new GitHub
    client_id = "<your client key>"
    client_secret = "<your client secret>"
    authorization_base_url = 'https://github.com/login/oauth/authorize'
    token_url = 'https://github.com/login/oauth/access_token'

    @app.route("/login")
    async def login():
        github = OAuth2Session(client_id)
        authorization_url, state = github.authorization_url(authorization_base_url)

        # State is used to prevent CSRF, keep this for later.
        session['oauth_state'] = state
        return redirect(authorization_url)

    @app.route("/callback")
    async def callback():
        github = OAuth2Session(client_id, state=session['oauth_state'])
        token = await github.fetch_token(token_url, client_secret=client_secret, authorization_response=request.url)

        return jsonify((await github.get('https://api.github.com/user')).json())


The above is a truncated example. A full working example is available here:
:ref:`real_example`


Installation
============

Requests-OAuthlib can be installed with `pip <https://pip.pypa.io/>`_: ::

    $ pip install Async-OAuthlib


Getting Started:
================

.. toctree::
   :maxdepth: 2

   oauth1_workflow
   oauth2_workflow
   examples/examples

   api



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
