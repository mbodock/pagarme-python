# encoding: utf-8

import mock

from pagarme.card import Card
from pagarme.exceptions import PagarmeApiError

from .pagarme_test import PagarmeTestCase
from .mocks import fake_card_get, fake_card_error


class CardTestCase(PagarmeTestCase):
    @mock.patch('requests.post', mock.Mock(side_effect=fake_card_get))
    def test_create_card(self):
        card = Card(api_key='api_key', card_hash='hashcardlong')
        card.create()

    @mock.patch('requests.post', mock.Mock(side_effect=fake_card_get))
    def test_create_card_with_data(self):
        card = Card(api_key='api_key', card_number='4111111111111111', expiration_date=1215, holder_name='Test User')
        card.create()

    @mock.patch('requests.get', mock.Mock(side_effect=fake_card_get))
    def test_find_card_by_id(self):
        card = Card(api_key='api_key', id='cardid34j23l4')
        card.find_by_id()
        self.assertEqual(card.data['last_digits'], '8048')

    @mock.patch('requests.get', mock.Mock(side_effect=fake_card_error))
    def test_find_card_by_id_fail(self):
        card = Card(api_key='api_key', id='cardid34j23l4')
        with self.assertRaises(PagarmeApiError):
            card.find_by_id()

    def test_find_card_without_id(self):
        card = Card(api_key='api_key')
        with self.assertRaises(ValueError):
            card.find_by_id()
