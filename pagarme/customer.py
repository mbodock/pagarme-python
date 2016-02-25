# encoding: utf-8

from __future__ import unicode_literals

class Customer(object):

    def __init__(self, name=None, document_number=None, email=None,
                 address_street=None, address_neighborhood=None,
                 address_zipcode=None, address_street_number=None,
                 address_complementary=None, phone_ddd=None, phone_number=None):

        address_zipcode = address_zipcode.replace('.', '').replace('-', '') if address_zipcode else None
        document_number = document_number.replace('.', '').replace('-', '') if document_number else None
        self.data = {
            'name': name,
            'document_number': document_number,
            'email': email,
            'address_street': address_street,
            'address_neighborhood': address_neighborhood,
            'address_zipcode': address_zipcode,
            'address_street_number': address_street_number,
            'address_complementary': address_complementary,
            'phone_ddd': phone_ddd,
            'phone_number': phone_number,
        }

    def get_anti_fraud_data(self):
        d = {}
        for key, value in self.data.items():
            if value is None:
                continue
            elif 'address' in key:
                new_key = 'customer[address][{key}]'.format(key=key.replace('address_', ''))
            elif 'phone' in key:
                new_key = 'customer[phone][{key}]'.format(key=key.replace('phone_', ''))
            else:
                new_key = 'customer[{key}]'.format(key=key)
            d[new_key] = value
        return d
