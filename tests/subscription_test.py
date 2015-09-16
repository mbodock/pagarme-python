# encoding: utf-8

import mock

from pagarme.customer import Customer
from pagarme.exceptions import PagarmeApiError
from pagarme.subscription import Plan, Subscription, NotBoundException
from pagarme.transaction import Transaction

from .mocks import fake_request_list, fake_create_plan, fake_get_plan, fake_error_plan, fake_get_sub, fake_error_sub
from .pagarme_test import PagarmeTestCase


class PlanTestCase(PagarmeTestCase):

    @mock.patch('requests.post', mock.Mock(side_effect=fake_create_plan))
    def test_can_create(self):
        plan = Plan(api_key='api_key',
                    name='Test plan',
                    color='red'
                )
        plan.create()
        self.assertEqual(20112, plan.data['id'])

    def test_plan_invalid_payment_method(self):
        with self.assertRaises(ValueError):
            plan = Plan(api_key='api_key', name='Test Plan', color='red', payment_methods=['rice'])

    def test_plan_without_api_key(self):
        with self.assertRaises(ValueError):
            plan = Plan(name='Test Plan', color='red')

    @mock.patch('requests.get', mock.Mock(side_effect=fake_get_plan))
    def test_get_plan_by_id(self):
        plan = Plan(api_key='api_key')
        plan.find_by_id(20112)
        self.assertEqual(20112, plan.data['id'])

    @mock.patch('requests.get', mock.Mock(side_effect=fake_error_plan))
    def test_get_plan_by_id_error(self):
        plan = Plan(api_key='api_key')
        with self.assertRaises(PagarmeApiError):
            plan.find_by_id(20112)

    @mock.patch('requests.post', mock.Mock(side_effect=fake_error_plan))
    def test_create_plan_error(self):
        plan = Plan(api_key='api_key')
        with self.assertRaises(PagarmeApiError):
            plan.create()

class SubscriptionTestCase(PagarmeTestCase):

    @mock.patch('requests.post', mock.Mock(side_effect=fake_get_sub))
    def test_can_create(self):
        sub = Subscription(api_key='api_key',
                plan_id=20112,
                card_hash='longcardhash32432',
                customer=Customer(email='email@test.com'))
        sub.create()
        self.assertEqual(16892, sub.data['id'])

    @mock.patch('requests.post', mock.Mock(side_effect=fake_get_sub))
    def test_can_create_wiht_card_id(self):
        sub = Subscription(api_key='api_key',
                plan_id=20112,
                card_id='longcardid32432',
                customer=Customer(email='email@test.com'))
        sub.create()
        self.assertEqual(16892, sub.data['id'])

    @mock.patch('requests.post', mock.Mock(side_effect=fake_error_sub))
    def test_can_create_error(self):
        sub = Subscription(api_key='api_key',
                plan_id=20112,
                card_hash='longcardhash32432',
                customer=Customer(email='email@test.com'))
        with self.assertRaises(PagarmeApiError):
            sub.create()

    def test_subscription_without_api_key(self):
        with self.assertRaises(ValueError):
            sub = Subscription(
                plan_id=20112,
                card_hash='longcardhash32432',
                customer=Customer(email='email@test.com'))

    def test_subscription_without_invalid_plan_id(self):
        with self.assertRaises(ValueError):
            sub = Subscription(api_key='api_key',
                    plan_id=20.112,
                    card_hash='longcardhash32432',
                    customer=Customer(email='email@test.com'))

    def test_subscription_costumer_without_email(self):
        with self.assertRaises(ValueError):
            sub = Subscription(api_key='api_key',
                    plan_id=20112,
                    card_hash='longcardhash32432',
                    customer=Customer())

    @mock.patch('requests.get', mock.Mock(side_effect=fake_error_sub))
    def test_get_subscription_by_id_error(self):
        sub = Subscription(api_key='api_key')
        with self.assertRaises(PagarmeApiError):
            sub.find_by_id(16892)

    def test_cancel_unboud_subscription(self):
        sub = Subscription(api_key='api_key')
        with self.assertRaises(NotBoundException):
            sub.cancel()

    @mock.patch('requests.get', mock.Mock(side_effect=fake_get_sub))
    @mock.patch('requests.post', mock.Mock(side_effect=fake_get_sub))
    def test_cancel_subscription(self):
        sub = Subscription(api_key='api_key')
        sub.find_by_id(16892)
        sub.cancel()

    @mock.patch('requests.get', mock.Mock(side_effect=fake_get_sub))
    @mock.patch('requests.post', mock.Mock(side_effect=fake_error_sub))
    def test_cancel_subscription_error(self):
        sub = Subscription(api_key='api_key')
        sub.find_by_id(16892)
        with self.assertRaises(PagarmeApiError):
            sub.cancel()

    @mock.patch('requests.get', mock.Mock(side_effect=fake_request_list))
    def test_get_subscriptions_transactions(self):
        sub = Subscription(api_key='api_key')
        sub.data['id'] = 16892
        transactions = sub.transactions()
        self.assertIsInstance(transactions[0], Transaction)

    def test_get_subscriptions_transactions_unbounded(self):
        sub = Subscription(api_key='api_key')
        with self.assertRaises(NotBoundException):
            transactions = sub.transactions()

    @mock.patch('requests.get', mock.Mock(side_effect=fake_error_sub))
    def test_get_subscriptions_transactions_fails(self):
        sub = Subscription(api_key='api_key')
        sub.data['id'] = 16892
        with self.assertRaises(PagarmeApiError):
            transactions = sub.transactions()
