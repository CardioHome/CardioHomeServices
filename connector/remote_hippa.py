__author__ = 'Simon'

from connector import register
from config import hippa
from functools import partial

register = partial(register, server=hippa)


@register
def add_patient(user_id, data):
    pass


@register
def get_patient(user_id):
    pass