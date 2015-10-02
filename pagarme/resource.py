# encoding: utf-8

import json

from .exceptions import PagarmeApiError

class AbstractResource(object):
    def __init__(self):
        raise NotImplementedError

    def handle_response(self, data):
        self.data.update(data)

    def error(self, response):
        data = json.loads(response)
        e = data['errors'][0]
        error_string = e['type'] + ' - ' + e['message']
        raise PagarmeApiError(error_string)

    def create(self):
        url = self.BASE_URL
        pagarme_response = self.api.post(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(json.loads(pagarme_response.content))
        else:
            self.error(pagarme_response.content)

    def get_data(self):
        data = self.data.copy()
        data.pop('api_key', False)
        return data
