# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from connector import dispatch
import remote_data

# Create your views here.
@dispatch
def get_user(user_id):
    return user_id


@dispatch
def add_home(user_id, target_user_id, home_id):
    remote_data.add_sensor_data()


@dispatch
def edit_user(user_id, data):
    pass


@dispatch
def signup(username, password, reg_key, data={}):
    pass


@dispatch
def login(username, password):
    pass


@dispatch
def generate_reg_key(role, org=None):
    pass


@dispatch
def get_reg_key(key):
    pass