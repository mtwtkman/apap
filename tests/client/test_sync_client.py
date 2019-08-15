import unittest
from unittest import mock

import requests

from apap.method import Method


class SyncClientTestBase(unittest.TestCase):
    def _makeOne(self, api_base_url, header_map=None, **headers):
        from apap.client import SyncClient

        return SyncClient(api_base_url, header_map, **headers)


class TestSyncClientBuildRequest(SyncClientTestBase):
    def _callFUT(self, method):
        return self._makeOne("fuga")._build_request(method)

    def test_return_callable_which_is_requests_proxy(self):
        for m in ["Get", "Post", "Put", "Delete"]:
            subject = self._callFUT(getattr(Method, m))
            self.assertEqual(subject, getattr(requests, m.lower()))


class TestSyncClientRequest(SyncClientTestBase):
    def _callFUT(self, url, method, cookies, **payload):
        return self._makeOne("fuga")._request(url, method, cookies, **payload)

    def test_call__build_request(self):
        with mock.patch("apap.client.SyncClient._build_request") as M:
            self._callFUT("neko", Method.Get, {})
            self.assertEqual(M.call_count, 1)
