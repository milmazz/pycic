import pytest
from datetime import datetime

from pycic.report import Report
from .base import ResponseMock


def mockreturn(api_url, params, proxies):
    r = ResponseMock()
    return r


def test_report(monkeypatch):
    monkeypatch.setattr("requests.get", mockreturn)
    r = Report()
    assert r.get() == '{"private_gists": 419}'


def test_report_limit_filter(monkeypatch):
    monkeypatch.setattr("requests.get", mockreturn)
    r = Report()
    assert r.get(limit=2) == '{"private_gists": 419}'


def test_report_limit_filter_fail(monkeypatch):
    monkeypatch.setattr("requests.get", mockreturn)
    r = Report()
    with pytest.raises(TypeError):
        r.get(limit=-1)


def test_report_until_filter(monkeypatch):
    date = datetime(2013, 12, 23)
    monkeypatch.setattr("requests.get", mockreturn)
    r = Report()
    assert r.get(until=date) == '{"private_gists": 419}'


def test_report_until_filter_fail(monkeypatch):
    monkeypatch.setattr("requests.get", mockreturn)
    r = Report()
    with pytest.raises(TypeError):
        r.get(until="2013-12-23")
