# -*- coding: utf-8 -*-


class ResponseMock(object):
    def __init__(self, status_code=200, encoding="utf-8"):
        self.status_code = status_code
        self.encoding = encoding
        self.text = u'{"private_gists": 419}'

    def json(self, **kwargs):
        return self.text

    def raise_for_status(self):
        if 400 <= self.status_code < 600:
            raise requests.exceptions.HTTPError
