__author__ = 'Simon'

from connector import register
from config import data
from functools import partial

register = partial(register, server=data)


@register
def add_sensor_data(data):
    pass


@register
def get_data(home_id, start_time, end_time, data_type=()):
    pass