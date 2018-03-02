from connector import register
from config import notification
from functools import partial

register = partial(register, server=notification)


@register
def trig(home_id, data):
    pass


@register
def get_all_patient_triggers(home_id):
    pass


@register
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

