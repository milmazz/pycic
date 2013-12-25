import pytest

from pycic.group import Group
from .base import ResponseMock

def mockreturn(api_url, proxies):
    r = ResponseMock()
    return r

def test_group(monkeypatch):
    monkeypatch.setattr("requests.get", mockreturn)
    r = Group()
    assert r.get() == '{"private_gists": 419}'