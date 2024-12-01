"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    n = len(data)
    if not n:
        return True

    f0, f1 = 0, 1
    for i in data:
        if i != f1:
            return False
        f0, f1 = f1, f0 + f1
    return True
