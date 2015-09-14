# encoding: utf-8

import json
import requests

from .exceptions import PagarmeApiError

class Plan(object):
    BASE_URL = 'https://api.pagar.me/1/plans'

    def __init__(self, api_key='', name='', amount=None, days=None, installments=1, payment_methods=['boleto', 'credit_card'],
                 color=None, charges=1, trial_days=0, **kwargs):

        if not api_key:
            raise ValueError('You should suply an api_key')
        for payment_method in payment_methods:
            if payment_method not in ['boleto', 'credit_card']:
                raise ValueError('Invalid payment method, try a list with "boleto" and/or "credit_card"')

        self.data = {'api_key': api_key}
        self.data['name'] = name
        self.data['amount'] = amount
        self.data['installments'] = installments
        self.data['payment_methods'] = payment_methods
        self.data['color'] = color
        self.data['charges'] = charges
        self.data['trial_days'] = trial_days
        self.data['days'] = days

        self.data.update(kwargs)

    def handle_response(self, data):
        self.data.update(data)

    def error(self, response):
        data = json.loads(response)
        e = data['errors'][0]
        error_string = e['type'] + ' - ' + e['message']
        raise PagarmeApiError(error_string)

    def create(self):
        url = self.BASE_URL
        pagarme_response = requests.post(url, data=self.data)
        if pagarme_response.status_code == 200:
            self.handle_response(json.loads(pagarme_response.content))
        else:
            self.error(pagarme_response.content)

    def find_by_id(self, id):
        url = self.BASE_URL + '/' + str(id)
        data = {'api_key': self.data['api_key']}
        pagarme_response = requests.get(url, params=data)
        if pagarme_response.status_code == 200:
            self.handle_response(json.loads(pagarme_response.content))
        else:
            self.error(pagarme_response.content)


class Subscription(object):

    BASE_URL = 'https://api.pagar.me/1/subscriptions'

    def __init__(
            self,
            api_key=None,
            plan_id=None,
            card_id=None,
            card_hash=None,
            postback_url=None,
            customer=None,
            **kwargs):
        if not api_key:
            raise ValueError('Invalid api_key')
        if plan_id and not isinstance(plan_id, int):
            raise ValueError('plan_id should be a int')
        if customer and not customer.data['email']:
            raise ValueError('Customer email not found')

        self.data = {
            'api_key': api_key,
            'plan_id': plan_id,
            'card_hash': card_hash,
            'postback_url': postback_url,
        }
        self.customer = customer

        if card_hash:
            self.data['card_id'] = card_id
        else:
            self.data['card_hash'] = card_hash

        self.data.update(kwargs)

    def get_data(self):
        data = self.data
        if self.customer:
            data.update(self.customer.to_dict())
        return data

    def create(self):
        url = self.BASE_URL
        pagarme_response = requests.post(url, data=self.get_data())
        if pagarme_response.status_code == 200:
            self.handle_response(json.loads(pagarme_response.content))
        else:
            self.error(pagarme_response.content)

    def handle_response(self, data):
        self.data.update(data)

    def error(self, response):
        data = json.loads(response)
        e = data['errors'][0]
        error_string = e['type'] + u' - ' + e['message']
        error_string = error_string.encode('utf-8')
        raise PagarmeApiError(error_string)