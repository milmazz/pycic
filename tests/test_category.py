import pytest

from pycic.category import Category
from .base import ResponseMock

def mockreturn(api_url, proxies):
    r = ResponseMock()
    return r

def test_report(monkeypatch):
    monkeypatch.setattr("requests.get", mockreturn)
    r = Category()
    assert r.get() == '{"private_gists": 419}'