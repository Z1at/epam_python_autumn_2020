from lecture_01.hw.tasks.task05 import find_maximal_subarray_sum


def test_1():
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16


def test_2():
    assert find_maximal_subarray_sum([-1, -2, -3, -4], 2) == 0


def test_3():
    assert find_maximal_subarray_sum([1, 2, 4, 3, 5, 2, 56, 2, 6], 4) == 66
