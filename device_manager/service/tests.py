# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .views import *
from .models import *
from unittest.mock import patch
from django.test import TestCase
import remote_auth
import remote_data
import datetime
import uuid

# dependency injected functions

def _add_sensor_data(*args):
    return {
        'uuid': uuid.uuid4(),
        'home_id': 1,
        'data_type': 0,
        'int_val1': 95,
        'int_val2': None,
        'flt_val1': None,
        'flt_val2': None,
        'str_val': "",
        'device_create_time': datetime.datetime.now(),
    }


def _get_user(*args):
    return{
        'nick_name': 'Mary',
        'avatar': '',
        'django_user': None,
        'role': 0,
        'home': None,
        'organization': None,
        'tz': 'PST',
        'lang': 'en'
    }


def _get_home(*args):
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


class DeviceManagement(TestCase):
    def test_device_management(self):
        with patch('remote_data.add_sensor_data', new=_add_sensor_data):

            with patch('remote_auth.get_user', new=_get_user):
                user = remote_auth.get_user()

                with patch('remote_auth.get_home', new=_get_home):
                    home = remote_auth.get_home()
                    device_type = 0
                    data = {
                        'display_name': 'Cardiogram',
                        'status': 1,
                    }
                    uid = uuid.uuid4()

                    user_id = 0
                    home_id = 0

                    test_dic = {'display_name': 'Cardiogram',
                                'device_type': 0,
                                'status': 1,
                                'home_id': home_id,
                                'uuid': uid}

                    device = add_device_to_home(user_id, home_id, uid, device_type, data)

                    device_dic = {'display_name': device.display_name,
                                  'device_type': device.device_type,
                                  'status': device.status,
                                  'home_id': device.home_id,
                                  'uuid': device.uuid}

                    self.assertDictEqual(test_dic, device_dic)

                    device_create_time = datetime.datetime.now()
                    sensor_data = remote_data.add_sensor_data()
                    receive_data(sensor_data)

                    device = update_status(uid, 0)
                    self.assertEqual(device.status, 0)

                    data2 = {
                        'display_name': 'Smart fork',
                        'status': 1,
                    }

                    # add multiple devices and test retrieval
                    device2 = add_device_to_home(user_id, home_id, sensor_data['uuid'], 1, data2)
                    device_set = get_all_devices(home_id)

                    print(device_set)
