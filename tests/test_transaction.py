# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import httpretty

from pagarme import PagarMe
from pagarme.transaction import Transaction
from pagarme.customer import Customer
from pagarme.metadata import MetaData


class TestTransaction(unittest.TestCase):

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
        self.api_endpoint = 'https://api.pagar.me/1/transactions'

    @httpretty.activate
    def test_charge_with_card_hash(self):
        response = '''{
            "date_updated":"2014-12-22T14:57:59.000Z",
            "ip":"187.112.12.183",
            "boleto_barcode":null,
            "cost":0,
            "refuse_reason":null,
            "id":173525,
            "card_holder_name":"Jose da Silva",
            "postback_url":"http://requestb.in/1f81u721",
            "boleto_expiration_date":null,
            "nsu":null,
            "payment_method":"credit_card",
            "card_brand":"visa",
            "tid":null,
            "card_last_digits":"4448",
            "metadata":{

            },
            "status":"processing",
            "authorization_code":null,
            "object":"transaction",
            "phone":{
                "id":13126,
                "ddi":"55",
                "object":"phone",
                "number":"30713261",
                "ddd":"11"
            },
            "referer":"api_key",
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
            "status_reason":"acquirer",
            "subscription_id":null,
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
            "soft_descriptor":"Pagamento 1",
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
            "amount":10000,
            "boleto_url":null,
            "antifraud_score":null,
            "installments":"1",
            "date_created":"2014-12-22T14:57:59.000Z",
            "acquirer_response_code":null,
            "card_first_digits":"490172"
        }'''

        httpretty.register_uri(
            httpretty.POST,
            self.api_endpoint,
            body=response,
            status=200,
        )

        transaction = Transaction(
            amount='10000',
            customer=self.customer,
            postback_url='http://requestb.in/1f81u721',
            card_hash='card_hash',
            soft_descriptor='Pagamento 1'
        )
        transaction.charge()

        self.assertEqual(transaction.data['id'], 173525)

    @httpretty.activate
    def test_charge_with_card_id(self):
        response = '''
        {
            "date_updated":"2014-12-22T15:09:03.000Z",
            "ip":"187.112.12.183",
            "boleto_barcode":null,
            "cost":0,
            "refuse_reason":null,
            "id":173526,
            "card_holder_name":"Jose da Silva",
            "postback_url":"http://requestb.in/1f81u721",
            "boleto_expiration_date":null,
            "nsu":null,
            "payment_method":"credit_card",
            "card_brand":"visa",
            "tid":null,
            "card_last_digits":"4448",
            "metadata":{

            },
            "status":"processing",
            "authorization_code":null,
            "object":"transaction",
            "phone":{
                "id":13126,
                "ddi":"55",
                "object":"phone",
                "number":"30713261",
                "ddd":"11"
            },
            "referer":"api_key",
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
            "status_reason":"acquirer",
            "subscription_id":null,
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
            "soft_descriptor":"Pagamento 2",
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
            "amount":10000,
            "boleto_url":null,
            "antifraud_score":null,
            "installments":"1",
            "date_created":"2014-12-22T15:09:03.000Z",
            "acquirer_response_code":null,
            "card_first_digits":"490172"
        }
        '''

        httpretty.register_uri(
            httpretty.POST,
            self.api_endpoint,
            body=response,
            status=200,
        )

        transaction = Transaction(
            amount='10000',
            customer=self.customer,
            postback_url='http://requestb.in/1f81u721',
            card_id='card_ci3xq3kyu0000yd16rihoplu6',
            soft_descriptor='Pagamento 2'
        )
        transaction.charge()

        self.assertEqual(transaction.data['id'], 173526)

    @httpretty.activate
    def test_charge_with_boleto(self):
        response = '''
        {
            "date_updated":"2014-12-22T15:16:51.000Z",
            "ip":"187.112.12.183",
            "boleto_barcode":"1234 5678",
            "cost":0,
            "refuse_reason":null,
            "id":173527,
            "card_holder_name":null,
            "postback_url":"http://requestb.in/1f81u721",
            "boleto_expiration_date":"2014-12-29T02:00:00.000Z",
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
            "phone":{
                "id":13126,
                "ddi":"55",
                "object":"phone",
                "number":"30713261",
                "ddd":"11"
            },
            "referer":"api_key",
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
            "status_reason":"acquirer",
            "subscription_id":null,
            "card":null,
            "soft_descriptor":null,
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
            "amount":10000,
            "boleto_url":"https://pagar.me/",
            "antifraud_score":null,
            "installments":1,
            "date_created":"2014-12-22T15:16:51.000Z",
            "acquirer_response_code":null,
            "card_first_digits":null
        }
        '''

        httpretty.register_uri(
            httpretty.POST,
            self.api_endpoint,
            body=response,
            status=200,
        )

        transaction = Transaction(
            amount='10000',
            customer=self.customer,
            postback_url='http://requestb.in/1f81u721',
            payment_method='boleto'
        )
        transaction.charge()

        self.assertEqual(transaction.data['id'], 173527)

    @httpretty.activate
    def test_charge_with_metadata(self):
        response = '''
        {
            "date_updated":"2014-12-22T19:17:09.000Z",
            "ip":"187.112.12.183",
            "boleto_barcode":"1234 5678",
            "cost":0,
            "refuse_reason":null,
            "id":173540,
            "card_holder_name":null,
            "postback_url":"http://requestb.in/1f81u721",
            "boleto_expiration_date":"2014-12-29T02:00:00.000Z",
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
            "phone":{
                "id":13126,
                "ddi":"55",
                "object":"phone",
                "number":"30713261",
                "ddd":"11"
            },
            "referer":"api_key",
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
            "status_reason":"acquirer",
            "subscription_id":null,
            "card":null,
            "soft_descriptor":null,
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
            "amount":10000,
            "boleto_url":"https://pagar.me/",
            "antifraud_score":null,
            "installments":1,
            "date_created":"2014-12-22T19:17:09.000Z",
            "acquirer_response_code":null,
            "card_first_digits":null
        }
        '''

        httpretty.register_uri(
            httpretty.POST,
            self.api_endpoint,
            body=response,
            status=200,
        )

        transaction = Transaction(
            amount='10000',
            customer=self.customer,
            postback_url='http://requestb.in/1f81u721',
            payment_method='boleto',
            metadata=self.metadata
        )
        transaction.charge()

        self.assertEqual(transaction.data['id'], 173540)
        self.assertEqual(transaction.data['metadata']['order_id'], '123456')

    @httpretty.activate
    def test_find_by_id(self):
        response = '''
        {
            "date_updated":"2014-12-22T15:09:03.000Z",
            "ip":"187.112.12.183",
            "boleto_barcode":null,
            "cost":260,
            "refuse_reason":null,
            "id":173526,
            "card_holder_name":"Jose da Silva",
            "postback_url":"http://requestb.in/1f81u721",
            "boleto_expiration_date":null,
            "acquirer_name":"development",
            "nsu":1419260943444,
            "payment_method":"credit_card",
            "card_brand":"visa",
            "tid":1419260943444,
            "card_last_digits":"4448",
            "metadata":{

            },
            "status":"paid",
            "authorization_code":"564326",
            "object":"transaction",
            "phone":{
                "id":13126,
                "ddi":"55",
                "object":"phone",
                "number":"30713261",
                "ddd":"11"
            },
            "referer":"api_key",
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
            "status_reason":"acquirer",
            "subscription_id":null,
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
            "soft_descriptor":"Pagamento 2",
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
            "amount":10000,
            "boleto_url":null,
            "antifraud_score":71.86,
            "installments":1,
            "date_created":"2014-12-22T15:09:03.000Z",
            "acquirer_response_code":"00",
            "card_first_digits":"490172"
        }
        '''

        httpretty.register_uri(
            httpretty.GET,
            self.api_endpoint + '/173526',
            body=response,
            status=200,
        )

        transaction = Transaction()
        transaction.find_by_id(173526)
        self.assertEqual(transaction.data['id'], 173526)
