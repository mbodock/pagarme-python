# encoding: utf-8

import json
import requests

from .exceptions import PagarmeApiError


class AbstractResource(object):
    BASE_URL = None

    def __init__(self):
        self.data = {}
        raise NotImplementedError

    def handle_response(self, data):
        self.data.update(data)

    def response_to_json(self, response):
        try:
            return json.loads(response)
        except TypeError:
            return json.loads(response.decode('utf-8'))

    def error(self, response):
        data = self.response_to_json(response)
        e = data['errors'][0]
        error_string = e['type'] + ' - ' + e['message']
        raise PagarmeApiError(error_string)

    def create(self):
        url = self.BASE_URL
        pagarme_response = requests.post(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(json.loads(pagarme_response.content))
        else:
            self.error(pagarme_response.content)

    def get_data(self):
        return self.data
