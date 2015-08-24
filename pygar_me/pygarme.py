# encoding: utf-8

from .transaction import Transaction


class Pygarme(object):
    def __init__(self, api_key=None):
        if not api_key:
            raise ValueError('You should suply the api key.')
        self.api_key = api_key

    def start_transaction(self,
        amount=None,
        card_hash=None,
        payment_method='credit_card',
        installments=1,
        postback_url=None):

        if not amount:
            raise ValueError('You should suply the value')
        if not card_hash and payment_method == 'credit_card':
            raise ValueError('You should suply a card_hash')
        if payment_method not in ('credit_card', 'boleto'):
            raise ValueError('Invalid payment_method')
        if not installments:
            raise ValueError('Invalid installments')

        return Transaction(api_key=self.api_key, amount=amount, card_hash=card_hash, payment_method=payment_method, installments=installments, postback_url=postback_url)
