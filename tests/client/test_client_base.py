import unittest
from unittest import mock
import inspect
from inspect import Parameter

from apap.method import Method


class ClientBaseTestBase(unittest.TestCase):
    def _makeOne(self, api_base_url, header_map=None, **headers):
        from apap.client import ClientBase
        return ClientBase(api_base_url, header_map, **headers)


class TestClientBaseHeaders(ClientBaseTestBase):
    def _callFUT(self, header_map=None, **headers):
        return self._makeOne("fuga", header_map, **headers).headers

    def test_without_header_map(self):
        subject = self._callFUT()
        self.assertEqual(subject, {})

    def test_with_header_map(self):
        header_names = ["X-Custom-Header", "A-B"]
        header_vars = ["custom_header", "foo"]
        header_map = dict(zip(header_names, header_vars))
        values = [1, "x"]
        subject = self._callFUT(header_map, **dict(zip(header_vars, values)))
        self.assertEqual(
            subject,
            {k: val for k, _, val in zip(header_names, header_vars, values)},
        )


class TestClientBaseBuildParam(ClientBaseTestBase):
    def _callFUT(self, method, params=None):
        return self._makeOne("fuga")._build_param(method, params)

    def assertPathParam(self, subject):
        self.assertTrue("params" in subject)

    def assertDataParam(self, subject):
        self.assertTrue("data" in subject)

    def test_key_is_path_param(self):
        for m in ["Get", "Delete"]:
            subject = self._callFUT(getattr(Method, m))
            self.assertPathParam(subject)

    def test_key_is_data_param(self):
        for m in ["Post", "Put"]:
            subject = self._callFUT(getattr(Method, m))
            self.assertDataParam(subject)

    def test_without_param(self):
        for m in list(Method):
            subject = self._callFUT(m)
            self.assertEqual(list(subject.values()), [{}])

    def test_with_params(self):
        for m in list(Method):
            expected = {"minami": "mirei", "manaka": "laala"}
            subject = self._callFUT(m, expected)
            self.assertEqual(list(subject.values()), [expected])


class TestClientBaseBuildUrl(ClientBaseTestBase):
    def _callFUT(self, api_base_url, endpoint):
        return self._makeOne(api_base_url)._build_url(endpoint)

    def test_ok(self):
        api_base_url = "toudou"
        endpoint = "shion"
        subject = self._callFUT(api_base_url, endpoint)
        self.assertEqual(subject, "toudou/shion")


class TestClientBaseApplyPathParams(ClientBaseTestBase):
    def _callFUT(self, endpoint, **path_params):
        return self._makeOne('hoge')._apply_path_params(endpoint, **path_params)

    def test_ok(self):
        endpoint = "y/:path1/z/:path2/---"
        path_params = {"path1": "A", "path2": "B"}
        subject = self._callFUT(endpoint, **path_params)
        self.assertEqual(subject, "y/A/z/B/---")


class TestClientBaseRequest(ClientBaseTestBase):
    def _callFUT(self, url, method):
        return self._makeOne("fuga")._request(url, method)

    def test_raise_not_implemented_error(self):
        with self.assertRaises(NotImplementedError):
            self._callFUT("", Method.Get)


class TestClientBaseMethod(ClientBaseTestBase):
    def _callFUT(self, method, api_base_url, endpoint):
        return self._makeOne(api_base_url).method(method, endpoint)

    def test_return_callable_wchich_takes_payload(self):
        subject = inspect.signature(
            self._callFUT(Method.Post, "neko", "inu")
        ).parameters
        self.assertEqual(len(subject), 1)
        for v in subject.values():
            self.assertEqual(v.kind, Parameter.VAR_KEYWORD)

    def test_inner_func_calls__request(self):
        with mock.patch("apap.client.ClientBase._request") as M:
            api_base_url = "neko"
            endpoint = "inu"
            method = Method.Post
            payload = {"x": 1}
            self._callFUT(method, api_base_url, endpoint)(**payload)
            self.assertEqual(M.call_count, 1)
            self.assertEqual(
                M.call_args, [(f"{api_base_url}/{endpoint}", method), payload]
            )


class TestClientBaseMethodWithPathParams(ClientBaseTestBase):
    def _callFUT(self, method, api_base_url, endpoint):
        return self._makeOne(api_base_url).method_with_path_params(
            method, endpoint
        )

    def assertTakeOneKwarg(self, subject):
        self.assertEqual(len(subject), 1)
        for v in subject.values():
            self.assertEqual(v.kind, Parameter.VAR_KEYWORD)

    def test_return_callable_which_takes_path_params(self):
        subject = inspect.signature(self._callFUT(Method.Get, "neko", "inu")).parameters
        self.assertTakeOneKwarg(subject)

    def test_inner_func_return_callable_which_takes_payload(self):
        subject = inspect.signature(
            self._callFUT(Method.Get, "neko", "inu")()
        ).parameters
        self.assertTakeOneKwarg(subject)

    def test_deepest_func_calls_method(self):
        endpoint = 'cats/:name'
        params = {'name': 'nico'}
        with mock.patch("apap.client.ClientBase.method") as M, mock.patch("apap.client.ClientBase._apply_path_params") as M2:
            self._callFUT(Method.Get, "meth", endpoint)(**params)()
            self.assertEqual(M.call_count, 1)
            self.assertEqual(M2.call_count, 1)
            self.assertEqual(M2.call_args, [(endpoint,), params])
