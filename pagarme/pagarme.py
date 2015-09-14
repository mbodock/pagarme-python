# encoding: utf-8

import hashlib
import json
import requests

from .exceptions import PagarmeApiError
from .transaction import Transaction


class Pagarme(object):
    def __init__(self, api_key=None):
        if not api_key:
            raise ValueError('You should suply the api key.')
        self.api_key = api_key

    def start_transaction(
            self,
            amount=None,
            card_hash=None,
            payment_method='credit_card',
            installments=1,
            postback_url=None,
            **kwargs):

        if not amount:
            raise ValueError('You should suply the value')
        if not card_hash and payment_method == 'credit_card':
            raise ValueError('You should suply a card_hash')
        if payment_method not in ('credit_card', 'boleto'):
            raise ValueError('Invalid payment_method')
        if not installments:
            raise ValueError('Invalid installments')

        return Transaction(api_key=self.api_key, amount=amount, card_hash=card_hash, payment_method=payment_method, installments=installments, postback_url=postback_url, **kwargs)

    def error(self, response):
        data = json.loads(response)
        e = data['errors'][0]
        error_string = e['type'] + ' - ' + e['message']
        raise PagarmeApiError(error_string)

    def find_transaction_by_id(self, id):
        transaction = Transaction(api_key=self.api_key)
        transaction.find_by_id(id)
        return transaction

    def all_transactions(self, page=1, count=10):
        data = {
            'page': page,
            'count': count,
        }
        url = Transaction.BASE_URL + 'transactions'
        pagarme_response = requests.get(url, data=data)
        if pagarme_response.status_code != 200:
            self.error(pagarme_response.content)
        responses = json.loads(pagarme_response.content)
        transactions = []
        for response in responses:
            transaction = Transaction(api_key=self.api_key)
            transaction.handle_response(response)
            transactions.append(transaction)

        return transactions

    def validate_fingerprint(self, object_id, fingerprint):
        code = str(object_id) + '#' + self.api_key
        sha1_hash = hashlib.sha1(code).hexdigest()
        return fingerprint == sha1_hash
