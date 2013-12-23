from .base import BaseMethod


class Group(BaseMethod):
    """Retrieve all groups available in the account."""
    def __init__(self, base_url="http://api.cic.mx", version=0,
                 account="nl", proxies=None):
        BaseMethod.__init__(self, base_url, version, account, proxies)
        self.method = "groups"
