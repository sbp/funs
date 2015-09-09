__all__ = ["jsonp"]

import json

def jsonp(obj):
    if isinstance(obj, bytes):
        obj = obj.decode("utf-8")
    return json.loads(obj)
