# encoding: utf-8

import requests


class ApiClient(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def get_auth(self):
        return (self.api_key, 'x')

    def get(self, *args, **kwargs):
        return requests.get(auth=self.get_auth(), *args, **kwargs)

    def post(self, *args, **kwargs):
        return requests.post(auth=self.get_auth(), *args, **kwargs)
