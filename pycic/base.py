import requests


class BaseMethod(object):
    """Base class for the available methods in CIC's API."""

    def __init__(self, base_url=None, version=None, account=None,
                 proxies=None):
        """
        :param base_url: Base URL of the CIC API
        :type base_url: str or None
        :param version: Version of this API
        :type version: int or None
        :param account: Jurisdiction (possible values until now: nl and sal)
        :type account: str or None
        :param proxies: Dictionary that contains http/https proxies
        :type proxies: dict or None
        """
        self.base_url = base_url
        self.version = version
        self.account = account
        self.proxies = proxies
        self.method = None

    def _get_method_url(self):
        """Return an URI for the method specified."""
        formatter = "json"
        if self.method:
            url = "%s/%d/%s/%s.%s" % (self.base_url, self.version,
                                      self.account, self.method,
                                      formatter)
            request_url = requests.head(url, proxies=self.proxies)
            request_url.raise_for_status()
            return url
        else:
            raise TypeError

    def get(self):
        """Retrieve all the available entries for the method especified."""
        api_url = self._get_method_url()

        r = requests.get(api_url, proxies=self.proxies)

        r.raise_for_status()

        return r.json()

    def save(self):
        """Save reports, groups or categories via CIC's API"""
        raise NotImplementedError
