# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Customer(object):

    def __init__(self, name='', document_number='', email='',
                 address_street='', address_neighborhood='',
                 address_zipcode='', address_street_number='',
                 address_complementary='', phone_ddd='', phone_number=''):
        self.name = name
        self.document_number = document_number
        self.email = email
        self.address_street = address_street
        self.address_neighborhood = address_neighborhood
        self.address_zipcode = address_zipcode
        self.address_street_number = address_street_number
        self.address_complementary = address_complementary
        self.phone_ddd = phone_ddd
        self.phone_number = phone_number

    def to_dict(self):
        return {
            'customer[name]': self.name,
            'customer[document_number]': self.document_number,
            'customer[email]': self.email,
            'customer[address][street]': self.address_street,
            'customer[address][neighborhood]': self.address_neighborhood,
            'customer[address][zipcode]': self.address_zipcode,
            'customer[address][street_number]': self.address_street_number,
            'customer[address][complementary]': self.address_complementary,
            'customer[phone][ddd]': self.phone_ddd,
            'customer[phone][number]': self.phone_number
        }
