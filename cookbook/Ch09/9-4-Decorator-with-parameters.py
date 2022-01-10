from functools import wraps
import logging

def logged(level, name=None, message=None):
    '''
    This is a decorator with parameters.
    '''

    a = 0
    b = 0
    def decorator(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

add(1,2)
