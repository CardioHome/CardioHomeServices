# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from service.views import *
from unittest.mock import patch
from django.test import TestCase
import remote_auth
import remote_data


def myfunc():
    return {

    }


class DeviceManagement(TestCase):
    def test_device_management(self):
        with patch('remote_data.add_sensor_data', new=myfunc):
            remote_data.add_sensor_data()
            add_device_to_home(user_id, home_id, uuid, device_type, data={})

        remote_data.add_sensor_data