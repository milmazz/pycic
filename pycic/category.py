from .base import BaseMethod


class Category(BaseMethod):
    """Retrieve all categories available in the account."""
    def __init__(self, base_url="http://api.cic.mx", version=0, account="nl"):
        BaseMethod.__init__(self, base_url, version, account)
        self.method = "categories"
