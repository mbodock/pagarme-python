# encoding: utf-8

import mock

from pygar_me.transaction import Transaction
from .pygarme_test import PygarmeTestCase


def fake_post(*args, **kwargs):
    class FakeResponse(object):
        status_code = 200
        content = '''
            {
                "object": "transaction",
                "status": "processing",
                "refuse_reason": null,
                "status_reason": "acquirer",
                "acquirer_response_code": null,
                "authorization_code": null,
                "soft_descriptor": "testeDeAPI",
                "tid": null,
                "nsu": null,
                "date_created": "2015-02-25T21:54:56.000Z",
                "date_updated": "2015-02-25T21:54:56.000Z",
                "amount": 314,
                "installments": 1,
                "id": 184220,
                "cost": 0,
                "postback_url": "",
                "payment_method": "credit_card",
                "antifraud_score": null,
                "boleto_url": null,
                "boleto_barcode": null,
                "boleto_expiration_date": null,
                "referer": "api_key",
                "ip": "189.8.94.42",
                "subscription_id": null,
                "phone": null,
                "address": null,
                "customer": null,
                "card": {
                    "object": "card",
                    "id": "card_ci6l9fx8f0042rt16rtb477gj",
                    "date_created": "2015-02-25T21:54:56.000Z",
                    "date_updated": "2015-02-25T21:54:56.000Z",
                    "brand": "mastercard",
                    "holder_name": "Api Customer",
                    "first_digits": "548045",
                    "last_digits": "3123",
                    "fingerprint": "HSiLJan2nqwn",
                    "valid": null
                },
                "metadata": {
                    "idProduto": "13933139"
                }
            }
        '''
    return FakeResponse()


class TransactionTestCase(PygarmeTestCase):

    @mock.patch('requests.post', mock.Mock(side_effect=fake_post))
    def test_charge(self):
        transaction = Transaction(amount=314, card_hash='foobar', payment_method='credit_card', installments=1, postback_url='https://post.back.url')
        transaction.charge()
        self.assertEqual('processing', transaction.status)
