from lecture_01.hw.tasks.task02 import check_fibonacci


def test_1():
    assert check_fibonacci([1, 1]) is True


def test_2():
    assert check_fibonacci([]) is True


def test_3():
    assert check_fibonacci([1, 1, 2, 3, 5, 8]) is True


def test_4():
    assert check_fibonacci([1, 1, 2, 4, 5]) is False


def test_5():
    assert check_fibonacci([1, 2, 3]) is False
