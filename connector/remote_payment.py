from connector import register
from config import payment
from functools import partial

register = partial(register, server=payment)


@register
def get_all_product():
    pass


@register
def create_transaction(sale_product, bill_info):
    pass


@register
def get_transaction(transaction_id):
    pass