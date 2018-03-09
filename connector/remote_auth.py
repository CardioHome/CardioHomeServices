__author__ = 'Simon'

from connector import register
from config import auth
from functools import partial

register = partial(register, server=auth)

@register
def get_user_id(token):
    pass

@register
def get_user(user_id):
    pass

@register
def add_user_to_home(user_id, target_user_id, home_id):
    pass

@register
def create_home(map_data):
    pass

@register
def get_home(home_id):
    pass

@register
def edit_user(user_id, data):
    pass

@register
def signup(username, password, email, reg_key, data={}):
    pass

@register
def login(username, password):
    pass

@register
def renew_token(token):
    pass

@register
def generate_reg_key(role, org_id, org=None):
    pass