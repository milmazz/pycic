"""Tests for Category and Group class."""

import pytest

from pycic.category import Category
from pycic.group import Group
from .base import mockreturn

@pytest.fixture(scope="function", params=[Category, Group])
def classarg(request):
    return request.param

def test_class_get(monkeypatch, classarg):
    monkeypatch.setattr("requests.get", mockreturn)
    monkeypatch.setattr("requests.head", mockreturn)
    r = classarg()
    assert r.get() ==  {
                        'categories': [
                            {
                                'id': 407,
                                'name': 'ACCIDENTE'
                            }
                        ]
                    }


def test_class_save(classarg):
    with pytest.raises(NotImplementedError):
        r = classarg()
        r.save()
