import json
import inspect
from urllib import request
import sys
import traceback

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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
            'result': result
        })
    except Exception as e:
        return JsonResponse({
            'error': traceback.format_exc()
        })

