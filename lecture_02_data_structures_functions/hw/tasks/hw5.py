"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import Any, List


def custom_range(iterable: Any, *args) -> List:
    iterable = [i for i in iterable]
    if len(args) == 1:
        ans = iterable[: iterable.index(args[0])]
    elif len(args) == 2:
        ans = iterable[iterable.index(args[0]): iterable.index(args[1])]
    elif len(args) == 3:
        ans = iterable[iterable.index(args[0]): iterable.index(args[1]): args[2]]
    else:
        raise ValueError("You can send maximum 3 arguments")

    return ans
