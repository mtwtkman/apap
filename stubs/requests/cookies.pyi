# Stubs for requests.cookies (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import abc
from ._internal_utils import to_native_string
from .compat import Morsel, MutableMapping, cookielib, urlparse, urlunparse
from typing import Any, Optional

class MockRequest:
    type: Any = ...
    def __init__(self, request: Any) -> None: ...
    def get_type(self): ...
    def get_host(self): ...
    def get_origin_req_host(self): ...
    def get_full_url(self): ...
    def is_unverifiable(self): ...
    def has_header(self, name: Any): ...
    def get_header(self, name: Any, default: Optional[Any] = ...): ...
    def add_header(self, key: Any, val: Any) -> None: ...
    def add_unredirected_header(self, name: Any, value: Any) -> None: ...
    def get_new_headers(self): ...
    @property
    def unverifiable(self): ...
    @property
    def origin_req_host(self): ...
    @property
    def host(self): ...

class MockResponse:
    def __init__(self, headers: Any) -> None: ...
    def info(self): ...
    def getheaders(self, name: Any) -> None: ...

def extract_cookies_to_jar(jar: Any, request: Any, response: Any) -> None: ...
def get_cookie_header(jar: Any, request: Any): ...
def remove_cookie_by_name(cookiejar: Any, name: Any, domain: Optional[Any] = ..., path: Optional[Any] = ...) -> None: ...

class CookieConflictError(RuntimeError): ...

class RequestsCookieJar(cookielib.CookieJar, MutableMapping, metaclass=abc.ABCMeta):
    def get(self, name: Any, default: Optional[Any] = ..., domain: Optional[Any] = ..., path: Optional[Any] = ...): ...
    def set(self, name: Any, value: Any, **kwargs: Any): ...
    def iterkeys(self) -> None: ...
    def keys(self): ...
    def itervalues(self) -> None: ...
    def values(self): ...
    def iteritems(self) -> None: ...
    def items(self): ...
    def list_domains(self): ...
    def list_paths(self): ...
    def multiple_domains(self): ...
    def get_dict(self, domain: Optional[Any] = ..., path: Optional[Any] = ...): ...
    def __contains__(self, name: Any): ...
    def __getitem__(self, name: Any): ...
    def __setitem__(self, name: Any, value: Any) -> None: ...
    def __delitem__(self, name: Any) -> None: ...
    def set_cookie(self, cookie: Any, *args: Any, **kwargs: Any): ...
    def update(self, other: Any) -> None: ...
    def copy(self): ...
    def get_policy(self): ...

def create_cookie(name: Any, value: Any, **kwargs: Any): ...
def morsel_to_cookie(morsel: Any): ...
def cookiejar_from_dict(cookie_dict: Any, cookiejar: Optional[Any] = ..., overwrite: bool = ...): ...
def merge_cookies(cookiejar: Any, cookies: Any): ...
