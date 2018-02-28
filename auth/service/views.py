# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
def get_user(user_id):
    pass


def add_home(user_id, target_user_id, home_id):
    pass


def edit_user(user_id, data):
    pass


def signup(username, password, reg_key, data={}):
    pass


def login(username, password):
    pass


def generate_reg_key(role, org=None):
    pass


def get_reg_key(key):
    pass