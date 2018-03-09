# -*- coding: utf-8 -*-
__author__ = ['Simon']
from __future__ import unicode_literals

from django.shortcuts import render

from connector import dispatch
# Create your views here.
@dispatch
def add_patient(user_id, data):
    pass


@dispatch
def get_patient(user_id):
    pass