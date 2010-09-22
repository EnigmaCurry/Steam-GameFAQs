from decorator import decorator
from pylons.decorators.util import get_pylons
import warnings
import json
import logging

log = logging.getLogger(__name__)

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        encoder = getattr(obj, '__json__', None)
        if encoder: return encoder()
        return super(JSONEncoder, self).default(obj)

@decorator
def jsonify(func, *args, **kwargs):
    """Action decorator that formats output for JSON

    Given a function that will return content, this decorator will turn
    the result into JSON, with a content-type of 'application/json' and
    output it.
    
    """
    pylons = get_pylons(args)
    pylons.response.headers['Content-Type'] = 'application/json'
    data = func(*args, **kwargs)
    if isinstance(data, (list, tuple)):
        msg = "JSON responses with Array envelopes are susceptible to " \
              "cross-site data leak attacks, see " \
              "http://pylonshq.com/warnings/JSONArray"
        warnings.warn(msg, Warning, 2)
        log.warning(msg)
    log.debug("Returning JSON wrapped action output")
    return json.dumps(data,cls=JSONEncoder)

def authorized(valid, handler):
    def validate(func, self, *args, **kwargs):
        try:
            valid.check()
        except NotValidAuth, e:
            return handler(e)
        return func(self, *args, **kwargs)
    return decorator(validate)
