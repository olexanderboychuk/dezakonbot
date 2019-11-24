import requests
from .conf import configuration

class ZakonApi:

    @classmethod
    def _request(cls, url):

        r = requests.get(url)

        return r.text

    @classmethod
    def get_registered(cls):

        return cls._request(configuration['registered_endpoint'])

    @classmethod
    def get_accepted(cls):

        return cls._request(configuration['accepted_endpoint'])