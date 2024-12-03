from lecture_02_data_structures_functions.hw.tasks.hw1 import *


def test_1():
    assert (get_longest_diverse_words(r"C:\Users\Zlat\Desktop\EPAM\epam_python_autumn_2020-main\lecture_02_data_structures_functions\hw\tests\materials\data.txt") ==
            [r'Bev\u00f6lkerungsabschub,', r'unmi\u00dfverst\u00e4ndliche', r'r\u00e9sistance-Bewegungen,', r'Werkst\u00e4ttenlandschaft',
             r'Werkst\u00e4ttenlandschaft', r'Selbstverst\u00e4ndlich', r'Machtbewu\u00dftsein,', r'Entz\u00fcndbarkeit.',
             r'Br\u00fcckenschl\u00e4gen;', r'Millionenbev\u00f6lkerung'])


def test_2():
    assert get_rarest_char(r"C:\Users\Zlat\Desktop\EPAM\epam_python_autumn_2020-main\lecture_02_data_structures_functions\hw\tests\materials\data.txt") == "Y"


def test_3():
    assert count_punctuation_chars(r"C:\Users\Zlat\Desktop\EPAM\epam_python_autumn_2020-main\lecture_02_data_structures_functions\hw\tests\materials\data.txt") == 5303


def test_4():
    assert count_non_ascii_chars(r"C:\Users\Zlat\Desktop\EPAM\epam_python_autumn_2020-main\lecture_02_data_structures_functions\hw\tests\materials\data.txt") == 2843


def test_5():
    assert get_most_common_non_ascii_char(r"C:\Users\Zlat\Desktop\EPAM\epam_python_autumn_2020-main\lecture_02_data_structures_functions\hw\tests\materials\data.txt") == 'da\\u00df'
