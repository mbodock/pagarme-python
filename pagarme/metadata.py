# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class MetaData(object):

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def to_dict(self):
        data = {}

        for k, v in self.kwargs.items():
            key = 'metadata[{0}]'.format(k)
            data[key] = v

        return data
