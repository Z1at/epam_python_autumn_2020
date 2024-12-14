from typing import Any, List

import pytest

from lecture_04_test.hw.tasks.task_5_optional import fizzbuzz


@pytest.mark.parametrize(
    ["number", "expected_values"],
    [
        (3, ["1", "2", "fizz"]),
        (5, ["1", "2", "fizz", "4", "buzz"]),
        (
            15,
            [
                "1",
                "2",
                "fizz",
                "4",
                "buzz",
                "fizz",
                "7",
                "8",
                "fizz",
                "buzz",
                "11",
                "fizz",
                "13",
                "14",
                "fizzbuzz",
            ],
        ),
    ],
)
def test_fizzbuzz(number: int, expected_values: List[Any]):

    assert all([el == expected_values[ind] for ind, el in enumerate(fizzbuzz(number))])
