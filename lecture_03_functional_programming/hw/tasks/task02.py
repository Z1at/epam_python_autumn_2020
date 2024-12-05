import time
import struct
import random
import hashlib

import _thread
from typing import Callable
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1,3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def calculate_time(func: Callable):
    sttime = time.time()
    print(func())
    entime = time.time()
    return entime - sttime


# basic instinct
def basic():
    ans = 0
    for i in range(20):
        ans += slow_calculate(i)
    return ans


# Неправильно работает
def some_threads():
    ans = 0
    for i in range(501):
        ans += _thread.start_new_thread(slow_calculate, (i, ))
    return ans


def multiprocessing():
    total_sum = 0
    if __name__ == "__main__":
        with Pool(45) as p:
            total_sum = sum(
                p.map(
                    slow_calculate,
                    list(range(501)),
                    chunksize=501 // 45,
                )
            )

    return total_sum


print(calculate_time(some_threads))
