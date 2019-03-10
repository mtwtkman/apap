import unittest


class TestDetectMethodName(unittest.TestCase):
    def _callFUT(self, url):
        from apap.client import detect_method_name

        return detect_method_name(url)

    def test_includes_format_symbol(self):
        subject = self._callFUT("hoge/:id")
        self.assertEqual(subject, "method_with_path_params")

    def test_not_include_format_symbol(self):
        subject = self._callFUT("hoge")
        self.assertEqual(subject, "method")
