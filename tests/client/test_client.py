import unittest

from apap.client import MethodMap
from apap.method import Method


class ClientTestBase(unittest.TestCase):
    def setUp(self):
        self.api_base_url = 'https://api/v1'

    def _makeOne(self, method_map, header_map=None, **headers):
        from apap.client import Client
        Client._method_map = method_map
        Client.api_base_url = self.api_base_url
        Client.header_map = header_map
        return Client(**headers)

    def test_generate_method(self):
        methods = [
            ("get_all", Method.Get, "resources"),
            ("get_one", Method.Get, "resources/:id"),
        ]
        method_map = MethodMap(*methods)
        one = self._makeOne(method_map)
        for m, _, _ in methods:
            self.assertTrue(hasattr(one, m))
            subject = getattr(one, m)

    def test_without_path_param(self):
        method_name = 'get_all'
        one = self._makeOne(MethodMap((method_name, Method.Get, 'resources')))
        subject = getattr(one, method_name)
        self.assertTrue('ClientBase.method.' in subject.__qualname__)

    def test_with_path_param(self):
        method_name = 'get_one'
        one = self._makeOne(MethodMap((method_name, Method.Get, 'resources/:id')))
        subject = getattr(one, method_name)
        self.assertTrue('ClientBase.method_with_path_params.' in subject.__qualname__)

