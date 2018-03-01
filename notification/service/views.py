# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def trig(home_id, data):
    pass


def get_all_patient_triggers(home_id):
    pass


def get_all_notifications(home_id, start_time=None, end_time=None):
    pass


def apply_trigger_to_patient(home_id, trigger_id):
    pass

def remove_trigger_from_patient(home_id, trigger_id):
    pass

def send_email(email, title, content):
    pass


def send_sms(phone_num, content):
    pass


def send_ios_app_notification(id, title, content, schedule_time=None):
    pass


def send_android_app_notification(id, title, content, schedule_time=None):
    pass

