__author__ = 'Simon'

from connector import register
from config import device_manager
from functools import partial

register = partial(register, server=device_manager)

@register
def add_device_to_home(user_id, uuid, device_type, data={}):
    pass

@register
def receive_data(uuid, data, device_create_time):
    pass


@register
def covert_device_to_patient_data():
    pass

@register
def update_status(uuid, status):
    pass


@register
def get_all_devices(online=True):
    pass