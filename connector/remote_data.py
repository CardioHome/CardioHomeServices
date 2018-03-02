from connector import register
from config import data
from functools import partial

register = partial(register, server=data)


@register
def add_sensor_data(device_uuid, home_id, data, type):
    pass


@register
def get_data(home_id, data_type=()):
    pass