# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .views import *

from unittest.mock import patch
from django.test import TestCase
import uuid
import datetime
import time

class DataAddAndRetrieve(TestCase):
    def test_data_add_and_retrieve(self):
        sensor_data = {
            'uuid': uuid.uuid4(),
            'home_id': 1,
            'data_type': 0,
            'int_val1': 95,
            'int_val2': None,
            'flt_val1': None,
            'flt_val2': None,
            'str_val': "",
            'device_create_time': datetime.datetime.now()
        }

        data = add_sensor_data(sensor_data)
        print(data)

        time.sleep(2)

        sensor_data2 = {
            'uuid': uuid.uuid4(),
            'home_id': 1,
            'data_type': 3,
            'int_val1': 1,
            'int_val2': 30,
            'flt_val1': None,
            'flt_val2': None,
            'str_val': "Jogging",
            'device_create_time': datetime.datetime.now()
        }
        data = add_sensor_data(sensor_data2)

        data_type = (0, 3)
        end_time = datetime.datetime.now()
        start_time = datetime.datetime.fromtimestamp(time.time() - 3)

        print(get_data(0, start_time, end_time, data_type))