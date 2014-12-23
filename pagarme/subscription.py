# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests

from pagarme import PagarMe


class Plan(PagarMe):

    def __init__(self, amount=None, days=None, name=None, trial_days=None,
                 charges=None, installments=None):
        self.amount = amount
        self.days = days
        self.name = name
        self.trial_days = trial_days
        self.charges = charges
        self.installments = installments
        self.data = {}

    def create(self):
        params = {
            'api_key': self.api_key,
            'amount': self.amount,
            'days': self.days,
            'name': self.name
        }

        if self.trial_days:
            params['trial_days'] = self.trial_days

        if self.charges:
            params['charges'] = self.charges

        if self.installments:
            params['installments'] = self.installments

        data = requests.post(
            self.api_endpoint + '/plans', data=params
        )

        self.data = data.json()

    def find_by_id(self, id):
        params = {
            'api_key': self.api_key
        }

        data = requests.get(
            self.api_endpoint + '/plans/{0}'.format(id), params=params
        )

        self.data = data.json()


class Subscription(PagarMe):

    def __init__(self, plan_id=None, card_hash=None, card_id=None,
                 customer=None, metadata=None, payment_method=None,
                 postback_url=None):
        self.plan_id = plan_id
        self.card_hash = card_hash
        self.card_id = card_id
        self.customer = customer
        self.metadata = metadata
        self.payment_method = payment_method
        self.postback_url = postback_url
        self.data = {}

    def create(self):
        params = {
            'api_key': self.api_key,
            'plan_id': self.plan_id,
        }

        if self.card_hash:
            params['card_hash'] = self.card_hash

        if self.card_id:
            params['card_id'] = self.card_id

        if self.customer:
            params.update(self.customer.to_dict())

        if self.metadata:
            params.update(self.metadata.to_dict())

        if self.payment_method:
            params['payment_method'] = self.payment_method

        if self.postback_url:
            params['postback_url'] = self.postback_url

        data = requests.post(
            self.api_endpoint + '/subscriptions', data=params
        )

        self.data = data.json()

    def find_by_id(self, id):
        params = {
            'api_key': self.api_key
        }

        data = requests.get(
            self.api_endpoint + '/subscriptions/{0}'.format(id), params=params
        )

        self.data = data.json()

    def cancel(self):
        id = self.data.get('id', None)

        if id:
            params = {
                'api_key': self.api_key
            }

            data = requests.post(
                self.api_endpoint + '/subscriptions/{0}/cancel'.format(id),
                data=params
            )

            self.data = data.json()
