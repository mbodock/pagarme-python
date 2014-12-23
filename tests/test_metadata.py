# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest

from pagarme.metadata import MetaData


class TestMetaData(unittest.TestCase):

    def test_to_dict(self):
        metadata = MetaData(
            metadata_1='MetaData 1',
            metadata_2='MetaData 2',
            metadata_3='MetaData 3',
            metadata_4='MetaData 4'
        )
        data = metadata.to_dict()
        self.assertEqual(
            data['metadata[metadata_1]'],
            'MetaData 1'
        )
        self.assertEqual(
            data['metadata[metadata_2]'],
            'MetaData 2'
        )
        self.assertEqual(
            data['metadata[metadata_3]'],
            'MetaData 3'
        )
        self.assertEqual(
            data['metadata[metadata_4]'],
            'MetaData 4'
        )
