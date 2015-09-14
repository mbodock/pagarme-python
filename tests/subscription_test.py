# encoding: utf-8

import mock

from pagarme.subscription import Plan, PagarmeApiError

from .mocks import fake_create_plan, fake_get_plan, fake_error_plan
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
