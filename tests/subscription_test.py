# encoding: utf-8

import mock

from pagarme.customer import Customer
from pagarme.subscription import Plan, PagarmeApiError, Subscription

from .mocks import fake_create_plan, fake_get_plan, fake_error_plan, fake_get_sub, fake_error_sub
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