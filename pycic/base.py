# -*- coding: utf-8 -*-

"""
Base method class definition.

This module implements the Base Method for new request to the CIC's API

"""

import requests


class BaseMethod(object):
    """Base class for the available methods in CIC's API."""

    def __init__(self, base_url=None, version=None, account=None,
                 proxies=None):
        """
        :param account: Jurisdiction (possible values until now: nl and sal)
        :type account: str or None
        :param base_url: Base URL of the CIC API
        :type base_url: str or None
        :param proxies: Dictionary that contains http/https proxies
        :type proxies: dict or None
        :param version: Version of this API
        :type version: int or None

        """
        self.account = account
        self.base_url = base_url
        self.method = None
        self.proxies = proxies
        self.version = version

    def _get_method_url(self):
        """Return an URI for the method specified."""
        formatter = "json"
        if self.method:
            url = "%s/%d/%s/%s.%s" % (self.base_url, self.version,
                                      self.account, self.method,
                                      formatter)
            request_url = requests.head(url, params=None, proxies=self.proxies)
            request_url.raise_for_status()
            return url
        else:
            raise TypeError

    def get(self, **kwargs):
        """Retrieve all the available entries for the method especified."""
        api_url = self._get_method_url()

        response = requests.get(api_url, params=None, proxies=self.proxies)

        response.raise_for_status()

        return response.json()

    def save(self):
        """Save reports, groups or categories via CIC's API"""
        raise NotImplementedError
