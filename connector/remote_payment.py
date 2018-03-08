from connector import register
from config import payment
from functools import partial

register = partial(register, server=payment)


@register
def get_all_product():
    pass


@register
def add_product(map_data):
    pass


@register
def edit_product(map_data):
    pass


@register
def get_product(display_name):
    pass


@register
def create_transaction(map_data):
    pass


@register
def get_transaction(transaction_id):
    pass

