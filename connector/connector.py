import json
import inspect
from urllib import request
import sys
import traceback
from uuid import UUID

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import model_to_dict
from django.db.models.fields.files import ImageFieldFile, FileField


def register(func, server):
    def wrap(*args, **argv):
        meta = {
            'name': func.__name__,
            'argv': argv,
            'args': args
        }
        bundle = json.dumps(meta)
        result = request.urlopen(server, data=bundle.encode('utf-8')).read()
        result = json.loads(result)
        if result['error']:
            print(result['error'])
            raise Exception()
        return result['result']

    return wrap


FuncMap = {}


def dispatch(func):
    def wrap(*args, **argv):
        return func(*args, **argv)
    #q(a=1)
    #q(1)
    FuncMap[func.__name__] = func
    return wrap


class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        if isinstance(obj, ImageFieldFile):
            return ''

        return json.JSONEncoder.default(self, obj)


def convert(data):
    if data is None or isinstance(data, str):
        return data
    elif isinstance(data, QuerySet) or isinstance(data, list):
        return [json.loads(json.dumps(model_to_dict(o), cls=Encoder)) for o in data]
    else:
        return json.loads(json.dumps(model_to_dict(data), cls=Encoder))

@csrf_exempt
def handler(req):
    bundle = json.loads(req.body.decode('utf-8'))
    name = bundle['name']
    argv = bundle['argv']
    args = bundle['args']
    if not FuncMap.get(name):
        return JsonResponse({
            'error': 'Function not found!'
        })

    try:
        result = FuncMap[name](*args, **argv)
        return JsonResponse({
            'error': '',
            'result': convert(result)
        })
    except Exception as e:
        return JsonResponse({
            'error': traceback.format_exc()
        })

