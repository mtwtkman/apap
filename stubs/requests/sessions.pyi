# Stubs for requests.sessions (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import time
from ._internal_utils import to_native_string
from .adapters import HTTPAdapter
from .auth import _basic_auth_str
from .compat import Mapping, OrderedDict, cookielib, is_py3, urljoin, urlparse
from .cookies import RequestsCookieJar, cookiejar_from_dict, extract_cookies_to_jar, merge_cookies
from .exceptions import ChunkedEncodingError, ContentDecodingError, InvalidSchema, TooManyRedirects
from .hooks import default_hooks, dispatch_hook
from .models import DEFAULT_REDIRECT_LIMIT, PreparedRequest, REDIRECT_STATI, Request
from .status_codes import codes
from .structures import CaseInsensitiveDict
from .utils import DEFAULT_PORTS, default_headers, get_auth_from_url, get_environ_proxies, get_netrc_auth, requote_uri, rewind_body, should_bypass_proxies, to_key_val_list
from typing import Any, Optional

preferred_clock: Any
preferred_clock = time.time

def merge_setting(request_setting: Any, session_setting: Any, dict_class: Any = ...): ...
def merge_hooks(request_hooks: Any, session_hooks: Any, dict_class: Any = ...): ...

class SessionRedirectMixin:
    def get_redirect_target(self, resp: Any): ...
    def should_strip_auth(self, old_url: Any, new_url: Any): ...
    def resolve_redirects(self, resp: Any, req: Any, stream: bool = ..., timeout: Optional[Any] = ..., verify: bool = ..., cert: Optional[Any] = ..., proxies: Optional[Any] = ..., yield_requests: bool = ..., **adapter_kwargs: Any) -> None: ...
    def rebuild_auth(self, prepared_request: Any, response: Any) -> None: ...
    def rebuild_proxies(self, prepared_request: Any, proxies: Any): ...
    def rebuild_method(self, prepared_request: Any, response: Any) -> None: ...

class Session(SessionRedirectMixin):
    __attrs__: Any = ...
    headers: Any = ...
    auth: Any = ...
    proxies: Any = ...
    hooks: Any = ...
    params: Any = ...
    stream: bool = ...
    verify: bool = ...
    cert: Any = ...
    max_redirects: Any = ...
    trust_env: bool = ...
    cookies: Any = ...
    adapters: Any = ...
    def __init__(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args: Any) -> None: ...
    def prepare_request(self, request: Any): ...
    def request(self, method: Any, url: Any, params: Optional[Any] = ..., data: Optional[Any] = ..., headers: Optional[Any] = ..., cookies: Optional[Any] = ..., files: Optional[Any] = ..., auth: Optional[Any] = ..., timeout: Optional[Any] = ..., allow_redirects: bool = ..., proxies: Optional[Any] = ..., hooks: Optional[Any] = ..., stream: Optional[Any] = ..., verify: Optional[Any] = ..., cert: Optional[Any] = ..., json: Optional[Any] = ...): ...
    def get(self, url: Any, **kwargs: Any): ...
    def options(self, url: Any, **kwargs: Any): ...
    def head(self, url: Any, **kwargs: Any): ...
    def post(self, url: Any, data: Optional[Any] = ..., json: Optional[Any] = ..., **kwargs: Any): ...
    def put(self, url: Any, data: Optional[Any] = ..., **kwargs: Any): ...
    def patch(self, url: Any, data: Optional[Any] = ..., **kwargs: Any): ...
    def delete(self, url: Any, **kwargs: Any): ...
    def send(self, request: Any, **kwargs: Any): ...
    def merge_environment_settings(self, url: Any, proxies: Any, stream: Any, verify: Any, cert: Any): ...
    def get_adapter(self, url: Any): ...
    def close(self) -> None: ...
    def mount(self, prefix: Any, adapter: Any) -> None: ...

def session(): ...
