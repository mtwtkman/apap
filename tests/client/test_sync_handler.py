import unittest
from unittest import mock

import requests

from apap.method import Method


class SyncHandlerTestBase(unittest.TestCase):
    def _makeOne(self, api_base_url, header_map=None, headers=None, cookies=None):
        from apap.client import SyncHandler

        return SyncHandler(api_base_url, header_map or {}, headers or {}, cookies or {})


class TestSyncHandlerBuildRequest(SyncHandlerTestBase):
    def _callFUT(self, method):
        return self._makeOne("fuga")._build_request(method)

    def test_return_callable_which_is_requests_proxy(self):
        for m in ["Get", "Post", "Put", "Delete"]:
            subject = self._callFUT(getattr(Method, m))
            self.assertEqual(subject, getattr(requests, m.lower()))


class TestSyncHandlerRequest(SyncHandlerTestBase):
    def _callFUT(self, url, method, cookies, **payload):
        return self._makeOne("fuga")._request(url, method, cookies, **payload)

    def test_call__build_request(self):
        with mock.patch("apap.client.SyncHandler._build_request") as M:
            self._callFUT("neko", Method.Get, {})
            self.assertEqual(M.call_count, 1)

    def test_pass_default_cookies(self):
        with mock.patch("apap.client.SyncHandler._build_request") as M:
            inner_mock = mock.Mock()
            M.return_value = inner_mock
            cookie = {"myid": "cookie-value"}
            self._callFUT("neko", Method.Get, cookie)
            _, kwargs = inner_mock.call_args
            self.assertTrue(kwargs == {"headers": {}, "cookies": cookie})
