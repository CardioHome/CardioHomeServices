# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import *

from connector import dispatch
import remote_auth

# Create your views here.
@dispatch
def add_sensor_data(device_uuid, home_id, data, data_type, device_create_time):
    """
    Adds a new sensor data specified by device with uuid to home with home_id
    :param device_uuid: 
    :param home_id: 
    :param data: 
    :param data_type:
    :param device_create_time
    :return: 
    """
    try:
        patient_data = PatientData.objects.all().filter(device_uuid=device_uuid, home_id=home_id, data_type=data_type)
        patient_data.device_create_time = device_create_time
        patient_data.save()
        data = PatientData(**data)
        data.save()
    except LookupError:
        return
    return data


@dispatch
def get_data(home_id, start_time, end_time, data_type=()):

    try:
        home = remote_auth.get_home(home_id)
        filtered_patient_data_set = []

        filtered_data_set = PatientData.objects.filter(data_type__in=data_type).\
                                                exclude(creation_time__gte=end_time).\
                                                filter(creation_time__gte=start_time)

        for data in filtered_data_set:
            filtered_patient_data_set.append({'device_uuid': data.device_uuid,
                                              'home_id': data.home_id,
                                              'data_type': data.data_type,
                                              'int_val1': data.int_val1,
                                              'int_val2': data.int_val2,
                                              'flt_val1': data.flt_val1,
                                              'flt_val2': data.flt_val2,
                                              'str_val': data.str_val,
                                              'device_create_time': data.device_create_time})
    except LookupError:
        return

    return filtered_patient_data_set
