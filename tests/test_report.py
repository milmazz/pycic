"""Tests for Report class."""

import pytest
from datetime import datetime

from pycic.report import Report
from .base import mockreturn


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.setattr("requests.get", mockreturn)
    monkeypatch.setattr("requests.head", mockreturn)


@pytest.fixture(scope="function", params=[{}, {"limit": 2},
                                          {"until": datetime(2013, 12, 23)}])
def get_success(request):
    return request.param

@pytest.fixture(scope="function", params=[{"limit": -1},
                                          {"until": "2013-12-23"}])
def get_fails(request):
    return request.param

def test_get_success(get_success):
    r = Report()
    assert r.get(**get_success) == '{"private_gists": 419}'

def test_get_fails(get_fails):
    r = Report()
    with pytest.raises(TypeError):
        r.get(**get_fails)


def test_save_fails():
    r = Report()
    with pytest.raises(NameError):
        r.save()


def test_save_category_type_error():
    r = Report()
    with pytest.raises(TypeError):
        r.save(category=494, content="raise TypeError")
