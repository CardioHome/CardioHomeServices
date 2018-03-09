# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from connector import dispatch
from .models import *
import remote_auth
import remote_data


@dispatch
def add_device_to_home(user_id, home_id, uuid, device_type, data={}):
    """
    Adds device with uuid specified with its type to the user with user_id.

    :param user_id:
    :param home_id:
    :param uuid: 
    :param device_type:
    :param data:
    :return: 
    """

    try:
        if not remote_auth.get_user(user_id) or not remote_auth.get_home(home_id):
            return

        device = Device(uuid=uuid, device_type=device_type, home_id=home_id, **data)
        device.save()
        return device
    except LookupError:
        return


@dispatch
def receive_data(data):
    """
    Receives the data of the device specified by uuid. Only receives the data if device w/ uuid exists in the 
    Device table.

    :param data:
    :return: data entry from the RawData table

    """
    try:
        device = Device.objects.all().filter(uuid=data['uuid'])[0]
        if not device:
            return
        raw_data = RawData(sensor=device, data=data)
        raw_data.save()
        processed_data = covert_device_to_patient_data(device, raw_data)

        # add data to data service
        remote_data.add_sensor_data(data)

    except LookupError:
        return

    return data


# Internal API function
def covert_device_to_patient_data(device, raw_data):

    device_type = device.device_type

    int_val1 = 0
    int_val2 = 0
    flt_val1 = 0.0
    flt_val2 = 0.0
    str_val = ''

    # cardiogram
    if device_type == 0:
        int_val1 = raw_data['heart rate']

    # smart fork
    elif device_type == 1:
        str_val = raw_data['food']
        int_val1 = raw_data['fat']
        int_val2 = raw_data['sodium']
        flt_val1 = raw_data['calories']

    # body temp sensor
    elif device_type is 2:
        flt_val1 = raw_data['temperature']

    # pill dispenser
    elif device_type is 3:
        str_val = raw_data['medicine_name']
        int_val1 = raw_data['amount']

    # stress sensor
    elif device_type is 4:
        int_val1 = raw_data['stress level']

    # exercise
    elif device_type is 5:
        str_val = raw_data['activity']
        int_val1 = raw_data['hours']
        int_val2 = raw_data['minutes']
    else:
        return

    processed_data = {'int_val1':int_val1, 'int_val2':int_val2,
                      'flt_val1':flt_val1, 'flt_val2':flt_val2, 'str_val':str_val}

    return processed_data


@dispatch
def update_status(uuid, status):
    """
    Updates the device status specified by the uuid.
    
    :param uuid: 
    :param status: 
    :return: 
    """
    try:
        device = Device.objects.all().filter(uuid=uuid)[0]
        device.status = status
        device.save()
        return device
    except LookupError:
        return


@dispatch
def get_all_devices(home_id):
    """
    Returns a list of devices within the home specified by home_id
    
    :param home_id: 
    :return: list of device objects from Device table
    """
    try:
        return Device.objects.all().filter(home_id=home_id)
    except LookupError:
        return


