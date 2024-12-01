from lecture_01.hw.tasks.task03 import find_maximum_and_minimum


def test_1():
    assert find_maximum_and_minimum(r"C:\Users\Zlat\Desktop\EPAM\epam_python_autumn_2020-main\lecture_01\hw\tests\materials\tst1") == (1, 5)


def test_2():
    assert find_maximum_and_minimum(r"C:\Users\Zlat\Desktop\EPAM\epam_python_autumn_2020-main\lecture_01\hw\tests\materials\tst2") == (1, 3456)


def test_3():
    assert find_maximum_and_minimum(r"C:\Users\Zlat\Desktop\EPAM\epam_python_autumn_2020-main\lecture_01\hw\tests\materials\tst3") == (-5, 5)


def test_4():
    assert find_maximum_and_minimum(r"C:\Users\Zlat\Desktop\EPAM\epam_python_autumn_2020-main\lecture_01\hw\tests\materials\tst4") == (2, 6)


def test_5():
    assert find_maximum_and_minimum(r"C:\Users\Zlat\Desktop\EPAM\epam_python_autumn_2020-main\lecture_01\hw\tests\materials\tst5") == (0, 0)
