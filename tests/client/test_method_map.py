import unittest

from apap.method import Method


class TestMethodMap(unittest.TestCase):
    def _makeOne(self, *tuples):
        from apap.client import MethodMap

        return MethodMap(*tuples)

    def test_no_tuple(self):
        one = self._makeOne()
        self.assertEqual(len(one.method_names), 0)

    def test_with_args(self):
        args = [("get", Method.Get, "a"), ("post", Method.Post, "a")]
        one = self._makeOne(*args)
        self.assertEqual(len(one.method_names), len(args))
        self.assertEqual(list(one.method_names), [x[0] for x in args])
