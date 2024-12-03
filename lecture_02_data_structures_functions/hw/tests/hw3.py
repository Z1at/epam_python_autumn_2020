from lecture_02_data_structures_functions.hw.tasks.hw3 import combinations


def test_1():
    assert (combinations([1, 2], [3, 4])) == [
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
    ]


def test_2():
    assert combinations([1, 2], [3]) == [
        [1, 3],
        [2, 3]
    ]


def test_3():
    assert combinations([1], [2]) == [[1, 2]]


def test_4():
    assert combinations([1], [2, 3], [4]) == [
        [1, 2, 4],
        [1, 3, 4]
    ]


def test_5():
    assert combinations([1, 2], [3, 4], [5, 6]) == [
        [1, 3, 5],
        [1, 3, 6],
        [1, 4, 5],
        [1, 4, 6],
        [2, 3, 5],
        [2, 3, 6],
        [2, 4, 5],
        [2, 4, 6]
    ]
