"""Tests for Report class."""

import pytest
from datetime import datetime

from pycic.report import Report
from pycic.exceptions import InvalidCategory
from .base import mockreturn

##############
# Parameters #
##############
get_success_params = [
    {},
    {"limit": 2},
    {"until": datetime(2013, 12, 23)},
    {"for_category": 407}
]

get_raises_type_error_params = [
    {"limit": "-1"},
    {"until": "2013-12-23"}
]

save_raises_type_error_params = [
    {
        "category": 404,
        "content": "TypeError"
    },
    {
        "category": "ACCIDENTE",
        "content": "TypeError",
        "lat": "123"
    }
]

save_raises_value_error_params = [
    {
        "category": "ACCIDENTE",
        "content": "ValueError",
        "return_path": "//developers.cic.mx/"
    },
    {
        "category": "ACCIDENTE",
        "content": "ValueError",
        "lat": 87,
        "lng": -190
    }
]

############
# Fixtures #
############
@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.setattr("requests.get", mockreturn)
    monkeypatch.setattr("requests.head", mockreturn)
    monkeypatch.setattr("requests.post", mockreturn)


@pytest.fixture(scope="function", params=get_success_params)
def get_success(request):
    return request.param


@pytest.fixture(scope="function", params=get_raises_type_error_params)
def get_raises_type_error(request):
    return request.param


@pytest.fixture(scope="function", params=save_raises_type_error_params)
def save_raises_type_error(request):
    return request.param


@pytest.fixture(scope="function", params=save_raises_value_error_params)
def save_raises_value_error(request):
    return request.param

#########
# Tests #
#########
def test__get_id_field_from_categories():
    r = Report()
    assert r._get_field_from_categories(field='id') == [407]


def test__get_field_from_categories_fails():
    r = Report()
    with pytest.raises(KeyError):
        r._get_field_from_categories()


def test_get_raise_for_category():
    r = Report()
    with pytest.raises(InvalidCategory):
        r.get(for_category="404")


def test_get_raises_type_error(get_raises_type_error):
    r = Report()
    with pytest.raises(TypeError):
        r.get(**get_raises_type_error)


def test_get_raises_value_error():
    r = Report()
    with pytest.raises(ValueError):
        r.get(limit=-1)


def test_get_success(get_success):
    output = {'categories': [{'id': 407, 'name': 'ACCIDENTE'}]}
    r = Report()
    assert r.get(**get_success) == output


def test_save_raises_name_error():
    r = Report()
    with pytest.raises(NameError):
        r.save()


def test_save_raises_type_error(save_raises_type_error):
    r = Report()
    with pytest.raises(TypeError):
        r.save(**save_raises_type_error)


def test_save_raises_value_error(save_raises_value_error):
    r = Report()
    with pytest.raises(ValueError):
        r.save(**save_raises_value_error)


def test_save_success():
    output = {'categories': [{'id': 407, 'name': 'ACCIDENTE'}]}
    params = {"category": "ACCIDENTE",
              "content": "Success",
              "video_url": "http://youtube.com",
              "lat": 87,
              "lng": 87.3}
    r = Report()

    r.save(**params) == output
