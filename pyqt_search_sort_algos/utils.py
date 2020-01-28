from functools import wraps
from time import time


def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print('Elapsed time{}: {}'.format(func,end-start))
        return result
    return wrapper