from lecture_02_data_structures_functions.hw.tasks.hw2 import major_and_minor_elem


def test_1():
    assert (major_and_minor_elem([3,2,3])) == (3, 2)


def test_2():
    assert major_and_minor_elem([2,2,1,1,1,2,2]) == (2, 1)


def test_3():
    assert major_and_minor_elem([1,1,1,1,1,1,1]) == (1, 1)


def test_4():
    assert major_and_minor_elem([1,2,3,4,5,6,6,6,2,2,1,1,1,1,1,1,1,1,1,4,1]) == (1, 3)


def test_5():
    assert major_and_minor_elem([4,4,4,4,4,4,4,3,3,3,2,2,1,2,2,3,3,3,4,4,4,4,4]) == (4, 1)
