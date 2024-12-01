"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    ans = 0
    ind = 0
    n = len(nums)
    while ind < n:
        if nums[ind] > 0:
            sm = sum(nums[ind: min(n, ind + k)])
            ans = max(ans, sm)
            for j in range(min(n, ind + k) - 1, ind, -1):
                sm -= nums[j]
                ans = max(ans, sm)
        ind += 1
    return ans
