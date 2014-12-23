# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest

from pagarme.customer import Customer


class TestCustomer(unittest.TestCase):

    def test_to_dict(self):
        customer = Customer(
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

        data = customer.to_dict()
        self.assertEqual(
            data['customer[name]'], 'John Appleseed'
        )
        self.assertEqual(
            data['customer[document_number]'], '92545278157'
        )
        self.assertEqual(
            data['customer[email]'], 'jappleseed@apple.com'
        )
        self.assertEqual(
            data['customer[address][street]'], 'Av. Brigadeiro Faria Lima'
        )
        self.assertEqual(
            data['customer[address][neighborhood]'], 'Jardim Paulistano'
        )
        self.assertEqual(
            data['customer[address][zipcode]'], '01452000'
        )
        self.assertEqual(
            data['customer[address][street_number]'], '2941'
        )
        self.assertEqual(
            data['customer[address][complementary]'], '8º andar'
        )
        self.assertEqual(
            data['customer[phone][ddd]'], '11'
        )
        self.assertEqual(
            data['customer[phone][number]'], '30713261'
        )
