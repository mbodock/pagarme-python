# encoding: utf-8

import mock
import unittest

from pagarme.customer import Customer
from pagarme.exceptions import PagarmeApiError
from pagarme.pagarme import Pagarme as CorrectlyPagarme
from pagarme.pagarme_facade import PagarmeFacade as Pagarme
from pagarme.resource import AbstractResource
from pagarme.transaction import Transaction

from .mocks import (
    fake_request,
    fake_request_fail,
    fake_request_list,
    fake_create_plan,
    fake_get_plan,
    fake_error_plan,
    fake_get_sub,
    fake_card_get,)


class PagarmeTestCase(unittest.TestCase):
    def setUp(self):
        self.api_key = 'keydeteste'

class AbstractResourceTestCase(PagarmeTestCase):
    def test_cant_instantiate_abstract_class(self):
        with self.assertRaises(NotImplementedError):
            AbstractResource()

class PagarmeApiTestCase(PagarmeTestCase):

    def test_can_instantiate(self):
        pagarme = Pagarme(self.api_key)
        self.assertIsInstance(pagarme, CorrectlyPagarme)

    def test_invalid_api(self):
        with self.assertRaises(ValueError):
            pagarme = Pagarme('')

    def test_start_transaction(self):
        pagarme = Pagarme(self.api_key)
        transaction = pagarme.start_transaction(amount=314, card_hash='hashcard')
        self.assertIsInstance(transaction, Transaction)

    def test_start_transaction_invalid_amount(self):
        pagarme = Pagarme(self.api_key)
        with self.assertRaises(ValueError):
            transaction = pagarme.start_transaction(amount=None, card_hash='hashcard')

    def test_start_transaction_invalid_card_hash(self):
        pagarme = Pagarme(self.api_key)
        with self.assertRaises(ValueError):
            transaction = pagarme.start_transaction(amount=314, card_hash='')

    def test_start_transaction_invalid_payment_method(self):
        pagarme = Pagarme(self.api_key)
        with self.assertRaises(ValueError):
            transaction = pagarme.start_transaction(amount=314, card_hash='hashcard', payment_method='rice_bag')

    def test_start_transaction_invalid_installments(self):
        pagarme = Pagarme(self.api_key)
        with self.assertRaises(ValueError):
            transaction = pagarme.start_transaction(amount=314, card_hash='hashcard', installments=0)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request))
    def test_find_transaction_by_id(self):
        pagarme = Pagarme(self.api_key)
        transaction = pagarme.find_transaction_by_id(314)
        self.assertIsInstance(transaction, Transaction)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_list))
    def test_get_all_transaction(self):
        pagarme = Pagarme(self.api_key)
        transactions = pagarme.all_transactions(page=2,count=3)
        self.assertTrue(len(transactions) == 1)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_fail))
    def test_get_all_transaction_fails(self):
        pagarme = Pagarme(self.api_key)
        with self.assertRaises(PagarmeApiError):
            transactions = pagarme.all_transactions(page=2,count=3)

    def test_validade_figerprint(self):
        pagarme = Pagarme(self.api_key)
        self.assertTrue(pagarme.validate_fingerprint(1, '7eaf1eae64ab8d91bcd2c315350a7e9b321808ee'))

    @mock.patch('requests.post', mock.Mock(side_effect=fake_create_plan))
    def test_create_plan(self):
        pagarme = Pagarme(self.api_key)
        plan = pagarme.start_plan(name='Test Plan', amount=314, days=30)
        plan.create()
        self.assertEqual(20112, plan.data['id'])

    def test_create_plan_without_amount(self):
        pagarme = Pagarme(self.api_key)
        with self.assertRaises(ValueError):
            pagarme.start_plan(name='Test Plan', amount=314)

    def test_create_plan_without_days(self):
        pagarme = Pagarme(self.api_key)
        with self.assertRaises(ValueError):
            pagarme.start_plan(name='Test Plan', days=30)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_get_plan))
    def test_find_plan_by_id(self):
        pagarme = Pagarme(self.api_key)
        plan = pagarme.find_plan_by_id(20112)
        self.assertEqual(20112, plan.data['id'])

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_list))
    def test_find_all_plans(self):
        pagarme = Pagarme(self.api_key)
        plans = pagarme.all_plans()
        self.assertIsInstance(plans, list)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_error_plan))
    def test_find_all_plans_error(self):
        pagarme = Pagarme(self.api_key)
        with self.assertRaises(PagarmeApiError):
            pagarme.all_plans()

    @mock.patch('requests.post', mock.Mock(side_effect=fake_get_sub))
    def test_create_subscription(self):
        pagarme = Pagarme(self.api_key)
        sub = pagarme.start_subscription(plan_id=20112, card_hash='hashcardlong', customer=Customer(email='teste@email.com'))
        sub.create()

    @mock.patch('requests.post', mock.Mock(side_effect=fake_get_sub))
    @mock.patch('requests.get', mock.Mock(side_effect=fake_get_plan))
    def test_create_subscription_with_plan(self):
        pagarme = Pagarme(self.api_key)
        plan = pagarme.find_plan_by_id(20112)
        sub = pagarme.start_subscription(plan=plan, card_hash='hashcardlong', customer=Customer(email='teste@email.com'))
        sub.create()

    @mock.patch('requests.get', mock.Mock(side_effect=fake_get_sub))
    def test_find_subscription_by_id(self):
        pagarme = Pagarme(self.api_key)
        sub = pagarme.find_subscription_by_id(16892)
        self.assertEqual(16892, sub.data['id'])

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_list))
    def test_find_all_subscriptions(self):
        pagarme = Pagarme(self.api_key)
        plans = pagarme.all_subscriptions()
        self.assertIsInstance(plans, list)

    @mock.patch('requests.get', mock.Mock(side_effect=fake_error_plan))
    def test_find_all_subscriptions_error(self):
        pagarme = Pagarme(self.api_key)
        with self.assertRaises(PagarmeApiError):
            pagarme.all_subscriptions()

    @mock.patch('requests.get', mock.Mock(side_effect=fake_card_get))
    def test_find_card_by_id(self):
        pagarme = Pagarme(self.api_key)
        card = pagarme.find_card_by_id('card_ci6y37h16wrxsmzyi')
        self.assertEqual('card_ci6y37h16wrxsmzyi', card.id)


class PagarmeFacadeTestCase(PagarmeTestCase):
    def tearDown(self):
        Pagarme.api_key = None

    def test_call_without_api_key(self):
        with self.assertRaises(ValueError):
            Pagarme.find_transaction_by_id(1321)

    def test_call_start_transaction(self):
        Pagarme.api_key = 'api_key'
        transaction = Pagarme.start_transaction(amount=10, card_hash='ahsh', piranha='doida', mane='garrinha')
        self.assertIsInstance(transaction, Transaction)
