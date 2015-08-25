# encoding: utf-8


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
            "id": 314,
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

def fake_request(*args, **kwargs):
    return FakeResponse()

def fake_request_list(*args, **kwargs):
    fakeresponse = FakeResponse()
    fakeresponse.content = '[' + fakeresponse.content + ']'
    return fakeresponse

def fake_request_fail(*args, **kwargs):
    fake = FakeResponse()
    fake.content = """
    {"errors":[{
        "type":"action_forbidden",
        "parameter_name":null,
        "message":"api_key inv\xc3\xa1lida"}],
        "url":"/transactions/314","method":"get"
    }
    """
    fake.status_code = 400
    return fake

