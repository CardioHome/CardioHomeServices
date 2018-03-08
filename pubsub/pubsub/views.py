from urllib import request
import json

from django.core.cache import cache
from connector import dispatch


def __get_event(event_name):
    '''
    Internal function. Get event meta by an event_name
    :param event_name: string
    :return: list
    '''
    if not isinstance(event_name, str):
        raise TypeError()

    return cache.get_or_set('event_' + event_name, [])


def __get_all_events():
    '''
    Return all events
    :return: set
    '''
    return cache.get_or_set('all_events', set())


def __add_event(event_name):
    '''
    Add a event to pool
    :param event_name:string
    :return: bool
    '''
    pool = cache.get_or_set('all_events', set())
    pool.add(event_name)
    cache.set('all_events', pool)
    return True


def __remove_event(event_name):
    '''
    Remove a event to pool
    :param event_name:string
    :return: bool
    '''
    pool = cache.get_or_set('all_events', set())
    if event_name in pool:
        pool.remove(event_name)
        cache.set('all_events', pool)
    return True


def __add_event_subscriber(event_name, subscriber_id, callback_url):
    '''
    Set event meta
    :param event_name: string
    :param subscriber_id: int
    :param callback_url: string
    :return: bool
    '''
    event = cache.get_or_set('event_' + event_name, [])
    event.append({
        'subscriber_id': subscriber_id,
        'callback_url': callback_url
    })
    cache.set(event_name, event)
    return True


def __remove_event_subscriber(event_name, subscriber_id):
    '''
    Remove subscriber in an even
    :param event_name: string
    :param subscriber_id: int
    :return: bool
    '''
    event = cache.get_or_set('event_' + event_name, [])
    event = [e for e in event if not e['subscriber_id'] == subscriber_id]
    if not event:
        __remove_event(event_name)
    cache.set(event_name, event)
    return True


@dispatch
def publish(publisher_id, event_name, data):
    '''
    Publish an event with data
    :param publisher_id: int
    :param event_name: string
    :param data: any json serializable object
    :return: bool
    '''
    urls = [e['callback_url'] for e in __get_event(event_name)]
    for url in urls:
        try:
            request.urlopen(url, data=json.loads(data).encode('UTF-8')).read()
        except Exception as e:
            import traceback
            traceback.print_exc()
    return True

@dispatch
def subscribe(subscriber_id, event_name, callback_url):
    '''
    Subscribe an event with a callback url
    :param subscriber_id: int
    :param event_name: string
    :param callback_url: an string
    :return: bool
    '''

    __add_event_subscriber(event_name, subscriber_id, callback_url)
    __add_event(event_name)
    return True




@dispatch
def unsubscribe(subscriber_id, event_name):
    '''
    Unsubcscribe an existing event
    :param subscriber_id: int
    :param event_name: string
    :return: bool
    '''
    return __remove_event_subscriber(event_name, subscriber_id)


@dispatch
def unsubscribe_all(subscriber_id):
    '''
    Unsubcscribe all events
    :param subscriber_id: int
    :return: bool
    '''
    event_names = __get_all_events()
    subscriber_events = [name for name in event_names for event in __get_event(name) if event['subscriber_id'] == subscriber_id]
    [__remove_event_subscriber(e, subscriber_id) for e in subscriber_events]
