from apap.client import Client, MethodMap
from apap.method import Method


class GithubApi(Client):
    api_base_url = 'https://api.github.com'
    header_map = {'Authorization': 'access_token'}


class Repository(GithubApi):
    name = 'repo'

    _method_map = MethodMap(
        ('get_one', Method.Get, 'users/:username/repos'),
    )


if __name__ == '__main__':
    import os

    import apap


    access_token = os.environ['GITHUB_ACCESS_TOKEN']
    username = os.environ['USERNAME']

    github_client = apap.apply(Repository)(access_token=f'token {access_token}')
    resp = github_client.repo.get_one(username=username)()
    print(resp.text)
    assert resp.status_code == 200
