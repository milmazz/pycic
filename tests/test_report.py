"""Tests for Report class."""

import pytest
from datetime import datetime

from pycic.report import Report
from pycic.exceptions import InvalidCategory
from .base import mockreturn

############
# Fixtures #
############


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.setattr("requests.get", mockreturn)
    monkeypatch.setattr("requests.head", mockreturn)


@pytest.fixture(scope="function", params=[{},
                                          {"limit": 2},
                                          {"until": datetime(2013, 12, 23)},
                                          {"for_category": 407}])
def get_success(request):
    return request.param

#########
# Tests #
#########


def test_get_id_field_from_categories():
    r = Report()
    r._get_field_from_categories(field='id') == 407


def test_get_field_from_categories_fails():
    r = Report()
    with pytest.raises(KeyError):
        r._get_field_from_categories()


def test_get_success(get_success):
    output = {'categories': [{'id': 407, 'name': 'ACCIDENTE'}]}
    r = Report()
    assert r.get(**get_success) == output


def test_raise_for_category():
    r = Report()
    with pytest.raises(InvalidCategory):
        r.get(for_category="404")


def test_raise_for_field():
    r = Report()
    with pytest.raises(TypeError):
        r.save(category=404, content="raise TypeError")


def test_raise_for_limit_type_error():
    r = Report()
    with pytest.raises(TypeError):
        r.get(limit="-1")


def test_raise_for_limit_value_error():
    r = Report()
    with pytest.raises(ValueError):
        r.get(limit=-1)


def test_raise_for_return_path():
    r = Report()
    with pytest.raises(ValueError):
        r.save(category="ACCIDENTE",
               content="raise ValueError",
               return_path="//developers.cic.mx/")


def test_raise_for_until():
    r = Report()
    with pytest.raises(TypeError):
        r.get(until="2013-12-23")


def test_save_fails():
    r = Report()
    with pytest.raises(NameError):
        r.save()


def test_save_success(monkeypatch):
    monkeypatch.setattr("requests.post", mockreturn)

    output = {'categories': [{'id': 407, 'name': 'ACCIDENTE'}]}
    params = {"category": "ACCIDENTE",
              "content": "Success",
              "video_url": "http://youtube.com"}
    r = Report()

    r.save(**params) == output
