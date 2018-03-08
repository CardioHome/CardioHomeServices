# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from service.views import *
from unittest.mock import patch
from django.test import TestCase
import remote_auth

def myfunc():
    return {
        'name': 'Mary\'s home',
        'state': '20',
        'city': 'Bothell',
        'zip_code': '98021',
        'address1': '1234 Somewhere Ave.',
        'address2': None,
        'size': '1500',
        'tz': 'PST',
    }


class DataAddAndRetrieve(TestCase):
    def test_data_add_and_retrieve(self):
        with patch('remote_auth.get_home', new=myfunc):
            remote_auth.get_home()