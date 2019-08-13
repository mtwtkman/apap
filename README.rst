|version| |ci-status|

.. |version| image:: https://img.shields.io/badge/python-3.7-blue.svg?style=flat
    :alt: version
    :scale: 100%
    :target: https://www.python.org/downloads/release/python-370/


.. |ci-status| image:: https://circleci.com/gh/mtwtkman/apap.svg?style=svg
    :alt: circleci status
    :scale: 100%
    :target: https://circleci.com/gh/mtwtkman/apap


Required
========

python3.7+

Example
=======

When you want to implement github api client, you just create a class which inherits `apap.Client` class.

.. code:: python

   import os

   from apap import MethodMap, Client, Method, apply


   class GithubAPI(Client):
      api_base_url = 'https://api.github.com'
      header_map = {'Authorization': 'access_token'}


   class Repo(GithubAPI):
      name = 'repo'

      _method_map = MethodMap(
         ('get_one', Method.Get, 'users/:username/repos'),
      )


   access_token = os.environ['ACCESS_TOKEN']
   username = os.environ['USERNAME']

   gh_client = apply(Repo)(access_token=f'token {access_token}')
   resp = gh_client.repo.get_one(username=username)()
   print(resp.text)
   assert resp.status_code == 200
