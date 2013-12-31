# -*- coding: utf-8 -*-

"""
Report class definition.

This module contains the Report class definition

"""

from datetime import datetime
try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

import requests

from .base import BaseMethod
from .category import Category
from .exceptions import InvalidCategory


class Report(BaseMethod):
    """Retrieve and save Reports."""

    def __init__(self, base_url="http://api.cic.mx", version=0,
                 account="nl", proxies=None):
        BaseMethod.__init__(self, base_url, version, account, proxies)
        self.category = None
        self.content = None
        self.first_name = None
        self.last_name = None
        self.lat = None
        self.limit = None
        self.lng = None
        self.method = "reports"
        self.return_path = None
        self.title = None
        self.until = None
        self.video_url = None

    def _get_field_from_categories(self, field=None):
        """Return specific field as a list for all categories.

        :param field: Some attribute for each category
        :type field: str
        :raises: KeyError

        """
        categories = Category(self.base_url, self.version, self.account)
        categories_filtered = []

        all_categories = categories.get()

        for category in all_categories["categories"]:
            category_field = category.get(field)
            if category_field:
                categories_filtered.append(category_field)
            else:
                raise KeyError

        return categories_filtered

    def get(self, **kwargs):
        """Retrieve reports, by default we get all the reports.

        :param limit: The total reports to get
        :type limit: int or None
        :param for_category: The ID of the category to filter.
        :type for_category: int or None
        :param until: Show previous reports to the date indicated
        :type until: datetime or None
        :returns: JSON object representation of the list of Reports
        :rtype: dict
        :raises: TypeError, ValueError, InvalidCategory

        """
        api_url = self._get_method_url()
        filter_category_by = "id"
        self.category = kwargs.get('for_category')
        self.limit = kwargs.get('limit')
        self.until = kwargs.get('until')

        # Validation process for fields
        if self.category:
            self.raise_for_category(filter_category_by)

        self.raise_for_limit()
        self.raise_for_until()

        payload = {"for_category": self.category,
                   "limit": self.limit,
                   "until": self.until
                   }

        response = requests.get(api_url, params=payload, proxies=self.proxies)

        response.raise_for_status()

        return response.json()

    def raise_for_category(self, field):
        """Raise InvalidCategory if one ocurred for category."""
        categories_field = self._get_field_from_categories(field)

        if not self.category in categories_field:
            raise InvalidCategory

    def raise_for_field(self, field, type_of_field):
        """Raise TypeError if occurred for field."""
        if field:
            if not isinstance(field, type_of_field):
                raise TypeError

    def raise_for_lat_or_lng(self, field, limits):
        """Raise ValueError if one ocurred for latitude or longitude fields."""
        if isinstance(field, (int, float)):
            if field < limits.get('min') or field > limits.get('max'):
                raise ValueError
        else:
            raise TypeError

    def raise_for_limit(self):
        """Raise ValueError or TypeError if one occurred for limit filter."""
        if self.limit:
            if isinstance(self.limit, int):
                if self.limit < 0:
                    raise ValueError
            else:
                raise TypeError

    def raise_for_return_path(self):
        """Raise ValueError if occurred for return_path field."""
        if self.return_path:
            url = urlparse(self.return_path)
            is_valid_scheme = (url.scheme == "http" or url.scheme == "https" or
                               url.scheme == "mailto")

            if not is_valid_scheme:
                raise ValueError

    def raise_for_until(self):
        """Raise TypeError if ocurred for until filter."""
        if self.until:
            if not isinstance(self.until, datetime):
                raise TypeError
            else:
                self.until = self.until.date().isoformat()

    def save(self, **kwargs):
        """Create report.

        :param title: Report title
        :type title: str
        :param content: Report content (required)
        :type content: str
        :param first_name: Report Contact, name of sender in string format
        :type first_name: str
        :param last_name: Report Contact, name of sender in string format.
        :type last_name: str
        :param return_path: Report Contact in URI format
                            Valid schemes supported: HTTP HTTPS MAILTO
        :type return_path: str
        :param lat: The report latitude in WGS84 decimal
        :type lat: float
        :param lng: The report longitude in WGS84 decimal
        :type lng: float
        :param video_url: Asset for the current report, the field accepts
                          a single string with an URL for a valid asset.
        :type video_url: str
        :param category: Send here the category name. You can get valid
                         names from Categories (required)
        :type category: str
        :raises: NameError, InvalidCategory, TypeError

        """

        api_url = self._get_method_url()
        filter_category_by = "name"
        self.category = kwargs.get('category')
        self.content = kwargs.get('content')
        self.first_name = kwargs.get('first_name')
        self.first_name = kwargs.get('last_name')
        self.lat = kwargs.get('lat')
        self.lng = kwargs.get('lng')
        self.return_path = kwargs.get('return_path')
        self.title = kwargs.get('title')
        self.video_url = kwargs.get('video_url')

        # Category and Content are required fields
        if not self.category or not self.content:
            raise NameError

        # Validation process for content, title, first_name,
        # last_name and category fields
        fields = [self.content, self.title, self.first_name,
                  self.last_name, self.category]
        for field in fields:
            self.raise_for_field(field, str)

        # Category name must be in uppercase
        self.category = self.category.upper()
        self.raise_for_category(filter_category_by)

        # Validation process for return_path field
        self.raise_for_return_path()

        # Validation process for video_url field
        if self.video_url:
            video_uri_response = requests.head(self.video_url,
                                               params=None,
                                               proxies=self.proxies)
            video_uri_response.raise_for_status()

        # Validation process for latitude or longitude fields
        if self.lat:
            self.raise_for_lat_or_lng(self.lat, {"min": -90, "max": 90})

        if self.lng:
            self.raise_for_lat_or_lng(self.lng, {"min": -180, "max": 180})

        payload = {
            "category": self.category,
            "content": self.content,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "lat": self.lat,
            "lng": self.lng,
            "return_path": self.return_path,
            "title": self.title,
            "video_url": self.video_url
        }

        response = requests.post(api_url, params=payload, proxies=self.proxies)

        response.raise_for_status()

        return response.json()
