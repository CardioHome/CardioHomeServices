# -*- coding: utf-8 -*-
__author__ = ['Simon']
from __future__ import unicode_literals

from django.shortcuts import render

from connector import dispatch
# Create your views here.
@dispatch
def trig(home_id, data):
    pass


@dispatch
def get_all_patient_triggers(home_id):
    pass


@dispatch
def get_all_notifications(home_id, start_time=None, end_time=None):
    pass


@dispatch
def apply_trigger_to_patient(home_id, trigger_id):
    pass


@dispatch
def remove_trigger_from_patient(home_id, trigger_id):
    pass


@dispatch
def send_email(email, title, content):
    pass


@dispatch
def send_sms(phone_num, content):
    pass


@dispatch
def send_ios_app_notification(id, title, content, schedule_time=None):
    pass


@dispatch
def send_android_app_notification(id, title, content, schedule_time=None):
    pass

