#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of the Kount python sdk project
# https://github.com/Kount/kount-ris-python-sdk/)
# Copyright (C) 2017 Kount Inc. All Rights Reserved.
"Test Xml Parser"
from __future__ import (
    absolute_import, unicode_literals, division, print_function)
import unittest
import os
from kount.settings import RESOURCE_FOLDER, XML_FILENAME
from kount.util.xmlparser import xml_to_dict
from kount.util.xml_dict import xml_dict

__author__ = "Yordanka Spahieva"
__version__ = "1.0.0"
__maintainer__ = "Yordanka Spahieva"
__email__ = "yordanka.spahieva@sirma.bg"
__status__ = "Development"

XML_FILENAME_PATH = os.path.join(os.path.dirname(__file__), '..',
                                 RESOURCE_FOLDER, XML_FILENAME)


class TestXmlParser(unittest.TestCase):
    "Test Xml Parser"
    def test_xml_to_dict(self):
        "test_xml_to_dict"
        self.maxDiff = None
        valid_data_dict, required_field_names, \
            notrequired_field_names = xml_to_dict(XML_FILENAME_PATH)
        expected_required_fields = [
            'VERS', 'MODE', 'MERC', 'SESS', 'CURR', 'TOTL',
            'CUSTOMER_ID', 'PTYP', 'IPAD', 'MACK', 'TRAN', 'PROD_TYPE',
            'PROD_ITEM', 'PROD_QUANT', 'PROD_PRICE', 'SITE', 'ANID']
        expected_not_required_fields = [
            'ORDR', 'CASH', 'EMAL', 'GENDER', 'DOB', 'NAME', 'B2A1',
            'B2A2', 'BPREMISE', 'BSTREET', 'B2CI', 'B2ST', 'B2CC',
            'B2PN', 'S2NM', 'S2EM', 'S2A1', 'S2A2', 'SPREMISE', 'SSTREET',
            'S2CI', 'S2ST', 'S2CC', 'S2PN', 'LAST4', 'UNIQ', 'EPOC',
            'UAGT', 'CAT1', 'CAT2', 'SHTP', 'AUTH', 'AVSZ', 'AVST',
            'CVVR', 'RFCB', 'PROD_DESC', 'B2PC', 'S2PC', 'FRMT']
        self.assertEqual(xml_dict, valid_data_dict)
        self.assertEqual(expected_required_fields, required_field_names)
        self.assertEqual(expected_not_required_fields, notrequired_field_names)


if __name__ == "__main__":
    unittest.main()
