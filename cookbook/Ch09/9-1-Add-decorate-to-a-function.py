
import time
from functools import wraps

def timethis(func, **kwargs):
    '''
    Decorator that reports the execution time
    '''

    @wraps(func)
    def wrapper1(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
    return wrapper1


@timethis
def countdown(n):
    '''
    Counts down
    '''

    while n > 0:
        n -= 1

countdown(100000)

countdown(10000000)