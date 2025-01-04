"""
Classic tasks, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List
from collections import Counter


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    cnt = Counter(num1 + num2 for num1 in a for num2 in b)
    return sum(cnt[-(num3 + num4)] for num3 in c for num4 in d)
