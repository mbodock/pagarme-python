# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests

from pagarme import PagarMe


class Transaction(PagarMe):

    def __init__(self, amount=None, card_hash=None, card_id=None,
                 installments=1, payment_method='credit_card', customer=None,
                 postback_url=None, soft_descriptor=None, capture=True,
                 metadata=None):
        self.amount = amount
        self.card_hash = card_hash
        self.card_id = card_id
        self.installments = installments
        self.payment_method = payment_method
        self.customer = customer
        self.postback_url = postback_url
        self.soft_descriptor = soft_descriptor
        self.capture = capture
        self.metadata = metadata
        self.data = {}

    def charge(self):
        params = {
            'api_key': self.api_key,
            'amount': self.amount,
            'payment_method': self.payment_method
        }

        if self.postback_url:
            params['postback_url'] = self.postback_url

        if self.customer:
            params.update(self.customer.to_dict())

        if self.metadata:
            params.update(self.metadata.to_dict())

        if self.payment_method == 'credit_card':

            params['installments'] = self.installments
            params['capture'] = self.capture

            if self.soft_descriptor:
                params['soft_descriptor'] = self.soft_descriptor[:13]

            if self.card_hash:
                params['card_hash'] = self.card_hash

            if self.card_id:
                params['card_id'] = self.card_id

        data = requests.post(
            self.api_endpoint + '/transactions', data=params
        )

        self.data = data.json()

    def find_by_id(self, id):
        params = {
            'api_key': self.api_key
        }

        data = requests.get(
            self.api_endpoint + '/transactions/{0}'.format(id), params=params
        )

        self.data = data.json()
