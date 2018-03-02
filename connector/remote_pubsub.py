from connector import register
from config import pubsub
from functools import partial

register = partial(register, server=pubsub)


@register
def publish(publisher_id, event_name, data):
    pass


@register
def subscribe(subscriber_id, event_name, callback_url):
    pass


@register
def unsubscribe(subscriber_id, event_name):
    pass


@register
def unsubscribe_all(subscriber_id):
    pass