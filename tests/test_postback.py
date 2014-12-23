# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest

from pagarme import PagarMe
from pagarme.postback import PostBack


class TestPostBack(unittest.TestCase):

    def setUp(self):
        self.postback_data1 = {
            'old_status': 'waiting_payment',
            'event': 'transaction_status_changed',
            'desired_status': 'paid',
            'fingerprint': 'be3ebb6e743dbc39d3fdf2df867a984f83c989f1',
            'object': 'transaction',
            'current_status': 'paid',
            'id': 173675
        }
        self.postback_data2 = {
            'old_status': 'waiting_payment',
            'event': 'transaction_status_changed',
            'desired_status': 'paid',
            'fingerprint': 'b4f0bc081343830fddedd61c6996dcb608df6d1c',
            'object': 'transaction',
            'current_status': 'paid',
            'id': 173675
        }

    def test_is_valid(self):
        PagarMe.api_key = 'api_key'
        postback = PostBack(self.postback_data1)
        self.assertFalse(postback.is_valid())

        postback = PostBack(self.postback_data2)
        self.assertTrue(postback.is_valid())
