# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib

from pagarme import PagarMe


class PostBack(PagarMe):

    def __init__(self, data=None):
        self.data = data

    def is_valid(self):
        id = self.data.get('id', None)
        fingerprint = self.data.get('fingerprint', None)
        expected_fingerprint = hashlib.sha1(
            '{0}#{1}'.format(id, self.api_key).encode('utf-8')
        ).hexdigest()
        return expected_fingerprint == fingerprint
