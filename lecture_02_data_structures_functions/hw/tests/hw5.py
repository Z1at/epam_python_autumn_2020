import string
from typing import Any, List, Tuple

import pytest

from lecture_02_data_structures_functions.hw.tasks.hw5 import custom_range


@pytest.mark.parametrize(
    ["iterable", "borders_and_step", "expected_result"],
    [
        (string.ascii_lowercase, ("g",), ["a", "b", "c", "d", "e", "f"]),
        (string.ascii_lowercase, ("g", "n"), ["g", "h", "i", "j", "k", "l", "m"]),
        (string.ascii_lowercase, ("p", "g", -2), ["p", "n", "l", "j", "h"]),
        ([i for i in range(5)], (1,), [0]),
        ([i for i in range(5)], (0, 4, -1), []),
        ([i for i in range(5)], (0, 4, 1), [0, 1, 2, 3]),
    ],
)
def test_custom_range(iterable: Any, borders_and_step: Tuple, expected_result: List):
    actual_result = custom_range(iterable, *borders_and_step)

    assert actual_result == expected_result
