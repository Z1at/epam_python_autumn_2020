from lecture_01.hw.tasks.task04 import check_sum_of_four


def test_1():
    assert check_sum_of_four([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2


def test_2():
    assert check_sum_of_four([0], [0], [0], [0]) == 1


def test_3():
    assert check_sum_of_four([1, 2], [0, 1], [4, 3], [1, 2]) == 0

