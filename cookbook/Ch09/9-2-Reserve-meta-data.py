import time
from functools import wraps

def timethis(func):

    a = 0
    b = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        '''
        Decorator that reports the execution time
        '''
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
    return wrapper

@timethis
def countdown(n):
    '''
    Counts down
    '''

    while n > 0:
        n -= 1
        
countdown(1000000)

print(countdown.__name__)
print(countdown.__doc__)

print( dir(countdown) )

countdown(100000)
print('')
countdown.__wrapped__(100000)
print('')
countdown(100000)
print('')
