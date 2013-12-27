"""Tests for BaseMethod class"""

import pytest

from pycic.base import BaseMethod

def test_class_get_method_url():
    with pytest.raises(TypeError):
        r = BaseMethod()
        r._get_method_url()

def test_save():
    with pytest.raises(NotImplementedError):
        r = BaseMethod()
        r.save()