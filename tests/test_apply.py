import unittest

from apap.client import Client, MethodMap
from apap.method import Method


class TestApply(unittest.TestCase):
    def _callFUT(self, clients):
        import apap

        return apap.apply(clients)

    def test_ok(self):
        class Api(Client):
            api_base_url = "https://myapi/v1"
            header_map = {"X-My-Header": "my_header"}

        class Endpoint1(Api):
            name = "endoint1"
            _method_map = MethodMap(
                ("get", Method.Get, "endpoint1/resources"),
                ("get_all", Method.Get, "endpoint1/resources/{{id}}"),
            )

        class Endpoint2(Api):
            name = "endpoint2"
            _method_map = MethodMap(("post", Method.Post, "endpoin2/resources"))

        clients = [Endpoint1, Endpoint2]
        subject = self._callFUT(clients)(my_header="hoge")
        for c in clients:
            self.assertTrue(hasattr(subject, c.name))
