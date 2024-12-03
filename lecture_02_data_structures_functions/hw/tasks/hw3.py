"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import List, Any


def combinations(*args: List[Any]) -> List[List]:
    ans = []
    ln = len(args)
    pos = [0 for i in range(ln)]
    while pos[0] != len(args[0]):
        res = []
        for ind, value in enumerate(pos):
            res.append(args[ind][value])

        for i in range(ln - 1, -1, -1):
            pos[i] += 1
            if pos[i] == len(args[i]) and i != 0:
                pos[i] = 0
            else:
                break

        ans.append(res)

    return ans
