"""Client API for CIC (Centro Integracion Ciudadana) in Mexico."""

import requests
from datetime import datetime

from .base import BaseMethod
from .category import Category
from .exceptions import InvalidCategory


class Report(BaseMethod):
    def __init__(self, base_url="http://api.cic.mx", version=0,
                 account="nl", proxies=None):
        BaseMethod.__init__(self, base_url, version, account, proxies)
        self.method = "reports"

    def _get_field_from_categories(self, field=None):
        """Return specific field as a list for all categories.

        :param field: Some attribute for each category
        :type field: str
        :raises: TypeError

        """
        categories_filtered = []
        categories = Category(self.base_url, self.version, self.account)

        all_categories = categories.get()

        for category in all_categories["categories"]:
            category_field = category.get(field)
            if category_field:
                categories_filtered.append(category_field)
            else:
                raise TypeError

        return categories_filtered

    def get(self, limit=None, for_category=None, until=None):
        """Retrieve reports, by default we get all the reports.

        :param limit: The total reports to get
        :type limit: int or None
        :param for_category: The ID of the category to filter.
        :type for_category: int or None
        :param until: Show previous reports to the date indicated
        :type until: datetime or None
        :returns: JSON object representation of the list of Reports
        :rtype: dict
        :raises: TypeError, InvalidCategory

        """
        api_url = self._get_method_url()

        date_filter = None

        if limit and (not isinstance(limit, int) or limit < 0):
            raise TypeError

        if for_category:
            field = "id"
            categories_id_field = self._get_field_from_categories(field)

            if not for_category in categories_id_field:
                raise InvalidCategory

        if until:
            if not isinstance(until, datetime):
                raise TypeError
            else:
                date_filter = until.date().isoformat()

        payload = {"limit": limit, "for_category": for_category,
                   "until": date_filter}

        r = requests.get(api_url, params=payload, proxies=self.proxies)

        if r.status_code == requests.codes.ok:
            return r.json()

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
        :param lat: The report latitude in WSG84 decimal
        :type lat: float
        :param lng: The report longitude in WSG84 decimal
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
        payload = kwargs

        if not payload.get('category') or not payload.get('content'):
            raise NameError

        # Validation process for category
        if isinstance(payload['category'], str):
            payload['category'] = payload['category'].upper()
            field = "name"
            categories_name_field = self._get_field_from_categories(field)

            if not payload['category'] in categories_name_field:
                raise InvalidCategory
        else:
            raise TypeError

        if payload.get('video_url'):
            video_uri_response = requests.head(payload['video_url'],
                                               proxies=self.proxies)
            video_uri_response.raise_for_status()

        r = requests.post(api_url, params=payload, proxies=self.proxies)

        r.raise_for_status()

        return r.json()
