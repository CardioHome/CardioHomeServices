# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from connector import dispatch

# Create your views here.
@dispatch
def receive_data(uuid, data):
    pass


@dispatch
def update_status(uuid, status):
    pass


@dispatch
def get_all_devices(online=True):
    pass