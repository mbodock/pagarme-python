# encoding: utf-8

"""
The MIT License (MIT)

Copyright (c) 2014 Allisson Azevedo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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
