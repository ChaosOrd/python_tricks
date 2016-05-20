from functools import wraps
import time


def timethis(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('Name: {}, Time: {}'.format(func.__name__, end-start))
        return result

    return wrapper


@timethis
def countdown(n):
    """
    Counts down
    :param n: The number to count from
    """
    while n > 0:
        n -= 1

countdown(10000)
