# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import *

from connector import dispatch
import remote_auth

# Create your views here.
@dispatch
def add_sensor_data(data):
    """
    Adds a new sensor data specified by device with uuid to home with home_id.

    :param data:
    :return: 
    """

    patient_data = PatientData(**data)
    patient_data.save()

    return data


@dispatch
def get_data(home_id, start_time, end_time, data_type=()):

    try:
        return list(PatientData.objects.filter(data_type__in=data_type, home_id=home_id). \
                                    filter(device_create_time__lte=end_time).\
                                   filter(device_create_time__gte=start_time))
    except LookupError:
        return


