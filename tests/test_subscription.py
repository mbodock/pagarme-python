# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import httpretty

from pagarme import PagarMe
from pagarme.customer import Customer
from pagarme.metadata import MetaData
from pagarme.subscription import Plan, Subscription


class TestPlan(unittest.TestCase):

    def setUp(self):
        PagarMe.api_key = 'ak_test_key'
        self.api_endpoint = 'https://api.pagar.me/1/plans'

    @httpretty.activate
    def test_create(self):
        response = '''
        {
            "name":"Meu Plano",
            "color":null,
            "object":"plan",
            "days":30,
            "payment_methods":[
                "boleto",
                "credit_card"
            ],
            "charges":"10",
            "amount":10000,
            "installments":"1",
            "trial_days":10,
            "date_created":"2014-12-23T12:19:19.000Z",
            "id":10848
        }
        '''

        httpretty.register_uri(
            httpretty.POST,
            self.api_endpoint,
            body=response,
            status=200,
        )

        plan = Plan(
            amount='10000', days=30, name='Meu Plano', trial_days=10,
            charges=10, installments=1
        )
        plan.create()
        self.assertEqual(plan.data['id'], 10848)

    @httpretty.activate
    def test_find_by_id(self):
        response = '''
        {
            "name":"Meu Plano",
            "color":null,
            "object":"plan",
            "days":30,
            "payment_methods":[
                "boleto",
                "credit_card"
            ],
            "charges":null,
            "amount":10000,
            "installments":1,
            "trial_days":0,
            "date_created":"2014-12-23T12:07:57.000Z",
            "id":10846
        }
        '''

        httpretty.register_uri(
            httpretty.GET,
            self.api_endpoint + '/10846',
            body=response,
            status=200,
        )

        plan = Plan()
        plan.find_by_id(10846)
        self.assertEqual(plan.data['id'], 10846)


class TestSubscription(unittest.TestCase):

    def setUp(self):
        PagarMe.api_key = 'ak_test_key'
        self.customer = Customer(
            name='John Appleseed',
            document_number='92545278157',
            email='jappleseed@apple.com',
            address_street='Av. Brigadeiro Faria Lima',
            address_neighborhood='Jardim Paulistano',
            address_zipcode='01452000',
            address_street_number='2941',
            address_complementary='8º andar',
            phone_ddd='11',
            phone_number='30713261'
        )
        self.metadata = MetaData(
            order_id='123456'
        )
        self.api_endpoint = 'https://api.pagar.me/1/subscriptions'

    @httpretty.activate
    def test_create_with_card_hash(self):
        response = '''
        {
            "status":"paid",
            "customer":{
                "name":"John Appleseed",
                "gender":null,
                "document_number":"92545278157",
                "object":"customer",
                "id":13683,
                "born_at":null,
                "date_created":"2014-12-21T01:15:21.000Z",
                "document_type":"cpf",
                "email":"jappleseed@apple.com"
            },
            "postback_url":"http://requestb.in/y3jcvey3",
            "phone":{
                "id":13126,
                "ddi":"55",
                "object":"phone",
                "number":"30713261",
                "ddd":"11"
            },
            "payment_method":"credit_card",
            "object":"subscription",
            "current_transaction":{
                "date_updated":"2014-12-23T13:09:53.000Z",
                "ip":"179.179.108.26",
                "boleto_barcode":null,
                "cost":260,
                "refuse_reason":null,
                "id":173611,
                "card_holder_name":"Jose da Silva",
                "postback_url":null,
                "boleto_expiration_date":null,
                "acquirer_name":"development",
                "nsu":"1419340193079",
                "payment_method":"credit_card",
                "card_brand":"visa",
                "tid":"1419340193079",
                "card_last_digits":"4448",
                "metadata":{

                },
                "status":"paid",
                "authorization_code":"635307",
                "object":"transaction",
                "referer":"api_key",
                "status_reason":"acquirer",
                "subscription_id":12215,
                "soft_descriptor":null,
                "amount":10000,
                "boleto_url":null,
                "antifraud_score":6.885,
                "installments":1,
                "date_created":"2014-12-23T13:09:52.000Z",
                "acquirer_response_code":"00",
                "card_first_digits":"490172"
            },
            "current_period_end":"2015-01-22T13:09:52.809Z",
            "current_period_start":"2014-12-23T13:09:52.809Z",
            "charges":0,
            "plan":{
                "name":"Meu Plano",
                "color":null,
                "object":"plan",
                "days":30,
                "payment_methods":[
                    "boleto",
                    "credit_card"
                ],
                "charges":null,
                "amount":10000,
                "installments":1,
                "trial_days":0,
                "date_created":"2014-12-23T12:07:57.000Z",
                "id":10846
            },
            "card_brand":"visa",
            "address":{
                "city":"S\\u00e3o Paulo",
                "neighborhood":"Jardim Paulistano",
                "street_number":"2941",
                "complementary":"8\\u00ba andar",
                "country":"Brasil",
                "object":"address",
                "zipcode":"01452000",
                "state":"SP",
                "street":"Av. Brigadeiro Faria Lima",
                "id":13236
            },
            "date_created":"2014-12-23T13:09:53.000Z",
            "card_last_digits":"4448",
            "id":12215,
            "card":{
                "holder_name":"Jose da Silva",
                "valid":true,
                "last_digits":"4448",
                "date_updated":"2014-12-21T01:15:22.000Z",
                "brand":"visa",
                "object":"card",
                "first_digits":"490172",
                "fingerprint":"2KnrHzAFkjPE",
                "date_created":"2014-12-21T01:15:21.000Z",
                "id":"card_ci3xq3kyu0000yd16rihoplu6"
            },
            "metadata":null
        }
        '''

        httpretty.register_uri(
            httpretty.POST,
            self.api_endpoint,
            body=response,
            status=200,
        )

        subscription = Subscription(
            plan_id=10846,
            card_hash='card_hash',
            customer=self.customer,
            postback_url='http://requestb.in/y3jcvey3'
        )
        subscription.create()
        self.assertEqual(subscription.data['id'], 12215)

    @httpretty.activate
    def test_create_with_card_id(self):
        response = '''
        {
            "status":"paid",
            "customer":{
                "name":"John Appleseed",
                "gender":null,
                "document_number":"92545278157",
                "object":"customer",
                "id":13683,
                "born_at":null,
                "date_created":"2014-12-21T01:15:21.000Z",
                "document_type":"cpf",
                "email":"jappleseed@apple.com"
            },
            "postback_url":"http://requestb.in/y3jcvey3",
            "phone":{
                "id":13126,
                "ddi":"55",
                "object":"phone",
                "number":"30713261",
                "ddd":"11"
            },
            "payment_method":"credit_card",
            "object":"subscription",
            "current_transaction":{
                "date_updated":"2014-12-23T13:15:47.000Z",
                "ip":"179.179.108.26",
                "boleto_barcode":null,
                "cost":260,
                "refuse_reason":null,
                "id":173612,
                "card_holder_name":"Jose da Silva",
                "postback_url":null,
                "boleto_expiration_date":null,
                "acquirer_name":"development",
                "nsu":"1419340547176",
                "payment_method":"credit_card",
                "card_brand":"visa",
                "tid":"1419340547176",
                "card_last_digits":"4448",
                "metadata":{

                },
                "status":"paid",
                "authorization_code":"191413",
                "object":"transaction",
                "referer":"api_key",
                "status_reason":"acquirer",
                "subscription_id":12216,
                "soft_descriptor":null,
                "amount":10000,
                "boleto_url":null,
                "antifraud_score":55.88,
                "installments":1,
                "date_created":"2014-12-23T13:15:47.000Z",
                "acquirer_response_code":"00",
                "card_first_digits":"490172"
            },
            "current_period_end":"2015-01-22T13:15:47.046Z",
            "current_period_start":"2014-12-23T13:15:47.046Z",
            "charges":0,
            "plan":{
                "name":"Meu Plano",
                "color":null,
                "object":"plan",
                "days":30,
                "payment_methods":[
                    "boleto",
                    "credit_card"
                ],
                "charges":null,
                "amount":10000,
                "installments":1,
                "trial_days":0,
                "date_created":"2014-12-23T12:07:57.000Z",
                "id":10846
            },
            "card_brand":"visa",
            "address":{
                "city":"S\\u00e3o Paulo",
                "neighborhood":"Jardim Paulistano",
                "street_number":"2941",
                "complementary":"8\\u00ba andar",
                "country":"Brasil",
                "object":"address",
                "zipcode":"01452000",
                "state":"SP",
                "street":"Av. Brigadeiro Faria Lima",
                "id":13236
            },
            "date_created":"2014-12-23T13:15:47.000Z",
            "card_last_digits":"4448",
            "id":12216,
            "card":{
                "holder_name":"Jose da Silva",
                "valid":true,
                "last_digits":"4448",
                "date_updated":"2014-12-21T01:15:22.000Z",
                "brand":"visa",
                "object":"card",
                "first_digits":"490172",
                "fingerprint":"2KnrHzAFkjPE",
                "date_created":"2014-12-21T01:15:21.000Z",
                "id":"card_ci3xq3kyu0000yd16rihoplu6"
            },
            "metadata":null
        }
        '''

        httpretty.register_uri(
            httpretty.POST,
            self.api_endpoint,
            body=response,
            status=200,
        )

        subscription = Subscription(
            plan_id=10846,
            card_id='card_id',
            customer=self.customer,
            postback_url='http://requestb.in/y3jcvey3'
        )
        subscription.create()
        self.assertEqual(subscription.data['id'], 12216)

    @httpretty.activate
    def test_create_with_boleto(self):
        response = '''
        {
            "status":"unpaid",
            "customer":{
                "name":"John Appleseed",
                "gender":null,
                "document_number":"92545278157",
                "object":"customer",
                "id":13683,
                "born_at":null,
                "date_created":"2014-12-21T01:15:21.000Z",
                "document_type":"cpf",
                "email":"jappleseed@apple.com"
            },
            "postback_url":"http://requestb.in/y3jcvey3",
            "phone":{
                "id":13126,
                "ddi":"55",
                "object":"phone",
                "number":"30713261",
                "ddd":"11"
            },
            "payment_method":"boleto",
            "object":"subscription",
            "current_transaction":{
                "date_updated":"2014-12-23T13:21:02.000Z",
                "ip":"179.179.108.26",
                "boleto_barcode":"1234 5678",
                "cost":0,
                "refuse_reason":null,
                "id":173614,
                "card_holder_name":null,
                "postback_url":null,
                "boleto_expiration_date":"2014-12-30T13:21:01.000Z",
                "acquirer_name":"development",
                "nsu":null,
                "payment_method":"boleto",
                "card_brand":null,
                "tid":null,
                "card_last_digits":null,
                "metadata":{

                },
                "status":"waiting_payment",
                "authorization_code":null,
                "object":"transaction",
                "referer":"api_key",
                "status_reason":"acquirer",
                "subscription_id":12217,
                "soft_descriptor":null,
                "amount":10000,
                "boleto_url":"https://pagar.me/",
                "antifraud_score":null,
                "installments":1,
                "date_created":"2014-12-23T13:21:01.000Z",
                "acquirer_response_code":null,
                "card_first_digits":null
            },
            "current_period_end":null,
            "current_period_start":null,
            "charges":0,
            "plan":{
                "name":"Meu Plano",
                "color":null,
                "object":"plan",
                "days":30,
                "payment_methods":[
                    "boleto",
                    "credit_card"
                ],
                "charges":null,
                "amount":10000,
                "installments":1,
                "trial_days":0,
                "date_created":"2014-12-23T12:07:57.000Z",
                "id":10846
            },
            "address":{
                "city":"S\\u00e3o Paulo",
                "neighborhood":"Jardim Paulistano",
                "street_number":"2941",
                "complementary":"8\\u00ba andar",
                "country":"Brasil",
                "object":"address",
                "zipcode":"01452000",
                "state":"SP",
                "street":"Av. Brigadeiro Faria Lima",
                "id":13236
            },
            "date_created":"2014-12-23T13:21:02.000Z",
            "id":12217,
            "card":null,
            "metadata":null
        }
        '''

        httpretty.register_uri(
            httpretty.POST,
            self.api_endpoint,
            body=response,
            status=200,
        )

        subscription = Subscription(
            plan_id=10846,
            payment_method='boleto',
            customer=self.customer,
            postback_url='http://requestb.in/y3jcvey3'
        )
        subscription.create()
        self.assertEqual(subscription.data['id'], 12217)

    @httpretty.activate
    def test_create_with_metadata(self):
        response = '''
        {
            "status":"unpaid",
            "customer":{
                "name":"John Appleseed",
                "gender":null,
                "document_number":"92545278157",
                "object":"customer",
                "id":13683,
                "born_at":null,
                "date_created":"2014-12-21T01:15:21.000Z",
                "document_type":"cpf",
                "email":"jappleseed@apple.com"
            },
            "postback_url":"http://requestb.in/y3jcvey3",
            "phone":{
                "id":13126,
                "ddi":"55",
                "object":"phone",
                "number":"30713261",
                "ddd":"11"
            },
            "payment_method":"boleto",
            "object":"subscription",
            "current_transaction":{
                "date_updated":"2014-12-23T13:26:00.000Z",
                "ip":"179.179.108.26",
                "boleto_barcode":"1234 5678",
                "cost":0,
                "refuse_reason":null,
                "id":173619,
                "card_holder_name":null,
                "postback_url":null,
                "boleto_expiration_date":"2014-12-30T13:26:00.000Z",
                "acquirer_name":"development",
                "nsu":null,
                "payment_method":"boleto",
                "card_brand":null,
                "tid":null,
                "card_last_digits":null,
                "metadata":{
                    "order_id":"123456"
                },
                "status":"waiting_payment",
                "authorization_code":null,
                "object":"transaction",
                "referer":"api_key",
                "status_reason":"acquirer",
                "subscription_id":12218,
                "soft_descriptor":null,
                "amount":10000,
                "boleto_url":"https://pagar.me/",
                "antifraud_score":null,
                "installments":1,
                "date_created":"2014-12-23T13:26:00.000Z",
                "acquirer_response_code":null,
                "card_first_digits":null
            },
            "current_period_end":null,
            "current_period_start":null,
            "charges":0,
            "plan":{
                "name":"Meu Plano",
                "color":null,
                "object":"plan",
                "days":30,
                "payment_methods":[
                    "boleto",
                    "credit_card"
                ],
                "charges":null,
                "amount":10000,
                "installments":1,
                "trial_days":0,
                "date_created":"2014-12-23T12:07:57.000Z",
                "id":10846
            },
            "address":{
                "city":"S\\u00e3o Paulo",
                "neighborhood":"Jardim Paulistano",
                "street_number":"2941",
                "complementary":"8\\u00ba andar",
                "country":"Brasil",
                "object":"address",
                "zipcode":"01452000",
                "state":"SP",
                "street":"Av. Brigadeiro Faria Lima",
                "id":13236
            },
            "date_created":"2014-12-23T13:26:00.000Z",
            "id":12218,
            "card":null,
            "metadata":{
                "order_id":"123456"
            }
        }
        '''

        httpretty.register_uri(
            httpretty.POST,
            self.api_endpoint,
            body=response,
            status=200,
        )

        subscription = Subscription(
            plan_id=10846,
            payment_method='boleto',
            customer=self.customer,
            postback_url='http://requestb.in/y3jcvey3',
            metadata=self.metadata
        )
        subscription.create()
        self.assertEqual(subscription.data['id'], 12218)
        self.assertEqual(subscription.data['metadata']['order_id'], '123456')

    @httpretty.activate
    def test_find_by_id(self):
        response = '''
        {
            "status":"unpaid",
            "customer":{
                "name":"John Appleseed",
                "gender":null,
                "document_number":"92545278157",
                "object":"customer",
                "id":13683,
                "born_at":null,
                "date_created":"2014-12-21T01:15:21.000Z",
                "document_type":"cpf",
                "email":"jappleseed@apple.com"
            },
            "postback_url":"http://requestb.in/y3jcvey3",
            "phone":{
                "id":13126,
                "ddi":"55",
                "object":"phone",
                "number":"30713261",
                "ddd":"11"
            },
            "payment_method":"boleto",
            "object":"subscription",
            "current_transaction":{
                "date_updated":"2014-12-23T13:26:00.000Z",
                "ip":"179.179.108.26",
                "boleto_barcode":"1234 5678",
                "cost":0,
                "refuse_reason":null,
                "id":173619,
                "card_holder_name":null,
                "postback_url":null,
                "boleto_expiration_date":"2014-12-30T13:26:00.000Z",
                "acquirer_name":"development",
                "nsu":null,
                "payment_method":"boleto",
                "card_brand":null,
                "tid":null,
                "card_last_digits":null,
                "metadata":{
                    "order_id":"123456"
                },
                "status":"waiting_payment",
                "authorization_code":null,
                "object":"transaction",
                "referer":"api_key",
                "status_reason":"acquirer",
                "subscription_id":12218,
                "soft_descriptor":null,
                "amount":10000,
                "boleto_url":"https://pagar.me/",
                "antifraud_score":null,
                "installments":1,
                "date_created":"2014-12-23T13:26:00.000Z",
                "acquirer_response_code":null,
                "card_first_digits":null
            },
            "current_period_end":null,
            "current_period_start":null,
            "charges":0,
            "plan":{
                "name":"Meu Plano",
                "color":null,
                "object":"plan",
                "days":30,
                "payment_methods":[
                    "boleto",
                    "credit_card"
                ],
                "charges":null,
                "amount":10000,
                "installments":1,
                "trial_days":0,
                "date_created":"2014-12-23T12:07:57.000Z",
                "id":10846
            },
            "address":{
                "city":"S\\u00e3o Paulo",
                "neighborhood":"Jardim Paulistano",
                "street_number":"2941",
                "complementary":"8\\u00ba andar",
                "country":"Brasil",
                "object":"address",
                "zipcode":"01452000",
                "state":"SP",
                "street":"Av. Brigadeiro Faria Lima",
                "id":13236
            },
            "date_created":"2014-12-23T13:26:00.000Z",
            "id":12218,
            "card":null,
            "metadata":{
                "order_id":"123456"
            }
        }
        '''

        httpretty.register_uri(
            httpretty.GET,
            self.api_endpoint + '/12218',
            body=response,
            status=200,
        )

        subscription = Subscription()
        subscription.find_by_id(12218)
        self.assertEqual(subscription.data['id'], 12218)

    @httpretty.activate
    def test_cancel(self):
        response = '''
        {
            "status":"unpaid",
            "customer":{
                "name":"John Appleseed",
                "gender":null,
                "document_number":"92545278157",
                "object":"customer",
                "id":13683,
                "born_at":null,
                "date_created":"2014-12-21T01:15:21.000Z",
                "document_type":"cpf",
                "email":"jappleseed@apple.com"
            },
            "postback_url":"http://requestb.in/y3jcvey3",
            "phone":{
                "id":13126,
                "ddi":"55",
                "object":"phone",
                "number":"30713261",
                "ddd":"11"
            },
            "payment_method":"boleto",
            "object":"subscription",
            "current_transaction":{
                "date_updated":"2014-12-23T13:26:00.000Z",
                "ip":"179.179.108.26",
                "boleto_barcode":"1234 5678",
                "cost":0,
                "refuse_reason":null,
                "id":173619,
                "card_holder_name":null,
                "postback_url":null,
                "boleto_expiration_date":"2014-12-30T13:26:00.000Z",
                "acquirer_name":"development",
                "nsu":null,
                "payment_method":"boleto",
                "card_brand":null,
                "tid":null,
                "card_last_digits":null,
                "metadata":{
                    "order_id":"123456"
                },
                "status":"waiting_payment",
                "authorization_code":null,
                "object":"transaction",
                "referer":"api_key",
                "status_reason":"acquirer",
                "subscription_id":12218,
                "soft_descriptor":null,
                "amount":10000,
                "boleto_url":"https://pagar.me/",
                "antifraud_score":null,
                "installments":1,
                "date_created":"2014-12-23T13:26:00.000Z",
                "acquirer_response_code":null,
                "card_first_digits":null
            },
            "current_period_end":null,
            "current_period_start":null,
            "charges":0,
            "plan":{
                "name":"Meu Plano",
                "color":null,
                "object":"plan",
                "days":30,
                "payment_methods":[
                    "boleto",
                    "credit_card"
                ],
                "charges":null,
                "amount":10000,
                "installments":1,
                "trial_days":0,
                "date_created":"2014-12-23T12:07:57.000Z",
                "id":10846
            },
            "address":{
                "city":"S\\u00e3o Paulo",
                "neighborhood":"Jardim Paulistano",
                "street_number":"2941",
                "complementary":"8\\u00ba andar",
                "country":"Brasil",
                "object":"address",
                "zipcode":"01452000",
                "state":"SP",
                "street":"Av. Brigadeiro Faria Lima",
                "id":13236
            },
            "date_created":"2014-12-23T13:26:00.000Z",
            "id":12218,
            "card":null,
            "metadata":{
                "order_id":"123456"
            }
        }
        '''

        response2 = '''
        {
            "status":"canceled",
            "customer":{
                "name":"John Appleseed",
                "gender":null,
                "document_number":"92545278157",
                "object":"customer",
                "id":13683,
                "born_at":null,
                "date_created":"2014-12-21T01:15:21.000Z",
                "document_type":"cpf",
                "email":"jappleseed@apple.com"
            },
            "postback_url":"http://requestb.in/y3jcvey3",
            "phone":{
                "id":13126,
                "ddi":"55",
                "object":"phone",
                "number":"30713261",
                "ddd":"11"
            },
            "payment_method":"boleto",
            "object":"subscription",
            "current_transaction":{
                "date_updated":"2014-12-23T13:26:00.000Z",
                "ip":"179.179.108.26",
                "boleto_barcode":"1234 5678",
                "cost":0,
                "refuse_reason":null,
                "id":173619,
                "card_holder_name":null,
                "postback_url":null,
                "boleto_expiration_date":"2014-12-30T13:26:00.000Z",
                "acquirer_name":"development",
                "nsu":null,
                "payment_method":"boleto",
                "card_brand":null,
                "tid":null,
                "card_last_digits":null,
                "metadata":{
                    "order_id":"123456"
                },
                "status":"waiting_payment",
                "authorization_code":null,
                "object":"transaction",
                "referer":"api_key",
                "status_reason":"acquirer",
                "subscription_id":12218,
                "soft_descriptor":null,
                "amount":10000,
                "boleto_url":"https://pagar.me/",
                "antifraud_score":null,
                "installments":1,
                "date_created":"2014-12-23T13:26:00.000Z",
                "acquirer_response_code":null,
                "card_first_digits":null
            },
            "current_period_end":null,
            "current_period_start":null,
            "charges":0,
            "plan":{
                "name":"Meu Plano",
                "color":null,
                "object":"plan",
                "days":30,
                "payment_methods":[
                    "boleto",
                    "credit_card"
                ],
                "charges":null,
                "amount":10000,
                "installments":1,
                "trial_days":0,
                "date_created":"2014-12-23T12:07:57.000Z",
                "id":10846
            },
            "card_brand":null,
            "address":{
                "city":"S\\u00e3o Paulo",
                "neighborhood":"Jardim Paulistano",
                "street_number":"2941",
                "complementary":"8\\u00ba andar",
                "country":"Brasil",
                "object":"address",
                "zipcode":"01452000",
                "state":"SP",
                "street":"Av. Brigadeiro Faria Lima",
                "id":13236
            },
            "date_created":"2014-12-23T13:26:00.000Z",
            "card_last_digits":null,
            "id":12218,
            "card":null,
            "metadata":{
                "order_id":"123456"
            }
        }
        '''

        httpretty.register_uri(
            httpretty.GET,
            self.api_endpoint + '/12218',
            body=response,
            status=200,
        )

        httpretty.register_uri(
            httpretty.POST,
            self.api_endpoint + '/12218/cancel',
            body=response2,
            status=200,
        )

        subscription = Subscription()
        subscription.find_by_id(12218)
        self.assertEqual(subscription.data['id'], 12218)
        subscription.cancel()
        self.assertEqual(subscription.data['id'], 12218)
        self.assertEqual(subscription.data['status'], 'canceled')
