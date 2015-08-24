# encoding: utf-8

import json
import requests


class Transaction(object):
    BASE_URL = 'https://api.pagar.me/1/'

    def __init__(self, api_key=None, amount=None, card_hash=None, payment_method='credit_card', installments=1, postback_url=None):
        self.amount = amount
        self.api_key = api_key
        self.card_hash = card_hash
        self.payment_method = payment_method
        self.installments = installments
        self.postback_url = postback_url

    def charge(self):
        post_data = self.get_data()
        transaction_url = self.BASE_URL + 'transactions'
        pagarme_response = requests.post(transaction_url, data=post_data)
        if pagarme_response.status_code == 200:
            self.handle_json_response(pagarme_response.content)
        else:
            # TODO implementar exception
            pass


    def handle_json_response(self, response):
        data = json.loads(response)
        self.status = data['status']
        self.card = data['card']
        self.postback_url = data['postback_url']
        self.metadata = data['metadata']
        self.response_data = data

    def get_data(self):
        return self.__dict__()

    def __dict__(self):
        d = {
            'api_key': self.api_key,
            'amount': self.amount,
            'card_hash': self.card_hash,
            'installments': self.installments,
            'payment_method': self.payment_method,
        }
        if self.postback_url:
            d['postback_url'] = self.postback_url
        return d
