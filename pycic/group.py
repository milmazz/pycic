# -*- coding: utf-8 -*-

"""
Group class definition.

This module contains the Group class definition

"""

from .base import BaseMethod


class Group(BaseMethod):
    """Retrieve all groups available in the account."""
    def __init__(self, base_url="http://api.cic.mx", version=0,
                 account="nl", proxies=None):
        BaseMethod.__init__(self, base_url, version, account, proxies)
        self.method = "groups"
