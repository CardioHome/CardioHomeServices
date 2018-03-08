from connector import dispatch
from django.core.cache import cache


@dispatch
def publish(publisher_id, event_name, data):
    pass


@dispatch
def subscribe(subscriber_id, event_name, callback_url):
    pass


@dispatch
def unsubscribe(subscriber_id, event_name):
    pass


@dispatch
def unsubscribe_all(subscriber_id):
    pass