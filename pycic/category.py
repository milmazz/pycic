# -*- coding: utf-8 -*-

"""
Category class definition.

This module contains the Category class definition

"""

from .base import BaseMethod


class Category(BaseMethod):
    """Retrieve all categories available in the account."""
    def __init__(self, base_url="http://api.cic.mx", version=0,
                 account="nl", proxies=None):
        BaseMethod.__init__(self, base_url, version, account, proxies)
        self.method = "categories"
