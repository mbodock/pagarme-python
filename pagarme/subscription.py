# encoding: utf-8

import json
import requests

from .exceptions import PagarmeApiError, PagarmeTransactionApiError, PagarmeTransactionError, NotPaidException, NotBoundException

class Plan(object):
    BASE_URL = 'https://api.pagar.me/1/'

    def __init__(self, api_key='', name='', installments=1, payment_methods=['boleto', 'credit_card'],
            color=None, charges=1, trial_days=0, **kwargs):

        if not api_key:
            raise ValueError('You should suply an api_key')
        for payment_method in payment_methods:
            if payment_method not in ['boleto', 'credit_card']:
                raise ValueError('Invalid payment method, try a list with "boleto" and/or "credit_card"')

        self.data = {'api_key': api_key}
        self.data['installments'] = installments
        self.data['payment_methods'] = payment_methods
        self.data['color'] = color
        self.data['charges'] = charges
        self.data['trial_days'] = trial_days

        self.data.update(kwargs)

    def handle_response(self, data):
        self.data.update(data)

        self.data['id'] = data['id']
        self.data['date_created'] = data['date_created']
        self.data['installments'] = data['installments']
        self.data['payment_methods'] = data['payment_methods']
        self.data['color'] = data['color']
        self.data['charges'] = data['charges']
        self.data['trial_days'] = data['trial_days']

    def error(self, response):
        data = json.loads(response)
        e = data['errors'][0]
        error_string = e['type'] + ' - ' + e['message']
        raise PagarmeApiError(error_string)

    def create(self):
        url = self.BASE_URL + 'plans'
        pagarme_response = requests.post(url, data=self.data)
        if pagarme_response.status_code == 200:
            self.handle_response(json.loads(pagarme_response.content))
        else:
            self.error(pagarme_response.content)


    def find_by_id(self, id):
        url = self.BASE_URL + 'plans/' + str(id)
        data = {'api_key': self.data['api_key']}
        pagarme_response = requests.get(url, params=data)
        if pagarme_response.status_code == 200:
            self.handle_response(json.loads(pagarme_response.content))
        else:
            self.error(pagarme_response.content)

