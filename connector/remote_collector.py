from connector import register
from config import collector
from functools import partial

register = partial(register, server=collector)

@register
def receive_data(uuid, data):
    pass


@register
def update_status(uuid, status):
    pass


@register
def get_all_devices(online=True):
    pass