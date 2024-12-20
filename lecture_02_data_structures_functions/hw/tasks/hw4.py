"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from typing import Callable


def cache(func: Callable) -> Callable:
    used_parameters = {}

    def cache_func(*args, **kwargs):
        parameters = args + tuple(kwargs.keys()) + tuple(kwargs.values())
        if parameters not in used_parameters:
            used_parameters[parameters] = func(*args, **kwargs)

        return used_parameters[parameters]

    return cache_func
