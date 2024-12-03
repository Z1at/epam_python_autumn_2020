"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    # Moore voting method: Boyer Moore voting algorithm
    mx = None
    count = 0
    for i in inp:
        if count == 0:
            mx = i
        elif mx != i:
            count -= 1
        else:
            count += 1

    voc = {}
    for i in inp:
        if i not in voc:
            voc[i] = 1
        else:
            voc[i] += 1

    mn = [1e15, 0]
    for i in voc:
        if voc[i] < mn[0]:
            mn[0] = voc[i]
            mn[1] = i

    return mx, mn[1]
