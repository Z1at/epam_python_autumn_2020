"""
In previous homework task 4,
you wrote a cache function that remembers other function output value.
Modify it to be a parametrized decorator, so that the following code:
@cache(times=3)
def some_function():
    pass
Would give out cached value up to times number only. Example:
@cache(times=2)
def f():
    return input('? ')   # careful with input() in python2, use raw_input() instead
>>> f()
? 1
'1'
>>> f()     # will remember previous value
'1'
>>> f()     # but use it up to two times only
'1'
>>> f()
? 2
'2'
"""
import functools
from typing import Callable


# def cache(times=0) -> Callable:
#     """Caches the function.
#
#     Args:
#         times: The number of times to return the cached value.
#
#     Returns:
#         Callable.
#
#     """
#
#     def cache_decorator(func: Callable) -> Callable:
#         """Cache decorator.
#
#         Args:
#             func: A function that needs to be cached.
#
#         Returns:
#             Callable.
#
#         """
#         used_parameters = {}
#
#         @functools.wraps(func)
#         def wrapper_function(*args, **kwargs):
#             all_of_the_parameters = args + tuple(kwargs.items())
#             if all_of_the_parameters not in used_parameters:
#                 used_parameters[all_of_the_parameters] = [
#                     func(*args, **kwargs),
#                     times - 1,
#                 ]
#             else:
#                 if used_parameters[all_of_the_parameters][1] != -1:
#                     used_parameters[all_of_the_parameters][1] -= 1
#                 else:
#                     used_parameters[all_of_the_parameters] = [
#                         func(*args, **kwargs),
#                         times - 1,
#                     ]
#
#             return used_parameters[all_of_the_parameters][0]
#
#         return wrapper_function
#
#     return cache_decorator


# Если мы хотим декоратор с параметрами, то нужно писать три функции
# Если мы хотим декоратор без параметров, то будет достаточно двух
def cache(times=0):
    def cache_decorator(func):
        value = times
        ans = ""

        def wrapper(*args, **kwargs):
            nonlocal value, ans
            if value == times:
                ans = func(*args, **kwargs)
            elif value == 0:
                value = times + 1
            value -= 1
            return ans

        return wrapper

    return cache_decorator


# @cache(2)
# def f():
#     return input("? ")


# @cache(3)
# def sm(a, b, c):
#     return a + b + c

# cached_func = cache(2)(f)

# print(f())
# print(f())
# print(f())
# print(f())
# print(f())

# while True:
#     print(f())


# while True:
#     a, b, c = map(int, input().split())
#     print(sm(a, b, c))

# print(cached_func())
# print(cached_func())
# print(cached_func())
# print(cached_func())
# print(cached_func())
