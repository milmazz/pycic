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
    assert r.get(**get_success) ==  {
                                        'categories': [
                                            {
                                                'id': 407,
                                                'name': 'ACCIDENTE'
                                            }
                                        ]
                                    }

def test_get_fails(get_fails):
    r = Report()
    with pytest.raises(TypeError):
        r.get(**get_fails)


def test_save_success(monkeypatch):
    monkeypatch.setattr("requests.post", mockreturn)
    r = Report()
    r.save(category="ACCIDENTE", content="Success") == {
                                                        'categories': [
                                                            {
                                                                'id': 407,
                                                                'name': 'ACCIDENTE'
                                                            }
                                                        ]
                                                    }

def test_save_fails():
    r = Report()
    with pytest.raises(NameError):
        r.save()


def test_save_category_type_error():
    r = Report()
    with pytest.raises(TypeError):
        r.save(category=494, content="raise TypeError")


def test_get_id_field_from_categories():
    r = Report()
    r._get_field_from_categories(field='id') == 407


def test_get_field_from_categories_fails():
    r = Report()
    with pytest.raises(TypeError):
        r._get_field_from_categories()


def test_invalid_return_path():
    r = Report()
    with pytest.raises(ValueError):
        r.save(category="ACCIDENTE",
               content="raise ValueError",
               return_path="//developers.cic.mx/")
