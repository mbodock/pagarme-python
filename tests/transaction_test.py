# encoding: utf-8

import mock

from pygar_me.transaction import Transaction, PygarmeTransactionApiError

from .mocks import fake_request, fake_request_fail
from .pygarme_test import PygarmeTestCase



class TransactionTestCase(PygarmeTestCase):

    @mock.patch('requests.post', mock.Mock(side_effect=fake_request))
    def test_charge(self):
        transaction = Transaction(api_key='apikey', amount=314, card_hash='foobar', payment_method='credit_card', installments=1, postback_url='https://post.back.url')
        transaction.charge()
        self.assertEqual('processing', transaction.status)

    @mock.patch('requests.post', mock.Mock(side_effect=fake_request_fail))
    def test_charge_fail(self):
        transaction = Transaction(api_key='apikey', amount=314, card_hash='foobar', payment_method='credit_card', installments=1, postback_url='https://post.back.url')
        with self.assertRaises(PygarmeTransactionApiError):
            transaction.charge()

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_get_transaction_by_id(self):
        transaction = Transaction(api_key='apikey')
        transaction.find_by_id(314)
        self.assertEqual(314, transaction.id)

    def test_get_transaction_by_id_with_invalid_id(self):
        transaction = Transaction(api_key='apikey')
        with self.assertRaises(ValueError):
            transaction.find_by_id('foo bar')

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail))
    def test_get_transaction_by_id_fails(self):
        transaction = Transaction(api_key='apikey')
        with self.assertRaises(PygarmeTransactionApiError):
            transaction.find_by_id(314)
