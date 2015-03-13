import requests
from os import path

from app.api.error import ItbookHttpError


def check_execption(func):
    def _check(*arg, **kws):
        r = func(*arg, **kws)
        if r.status_code >= 400:
            raise ItbookHttpError(r.status_code, r.text)
        return r
    return _check


class ItbooksApiBase:
    itbook_base_url = 'http://it-ebooks-api.info/v1'

    @check_execption
    def _get(self, url):
        return requests.get(path.join(self.itbook_base_url, url))
