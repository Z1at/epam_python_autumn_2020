from typing import Any, Callable, Dict, List

import pytest

from lecture_02_data_structures_functions.hw.tasks.hw4 import cache


def sum_of_parameters(a, b, c):
    return a + b + c


def args_len_plus_kwargs_len(*args, **kwargs):
    return len(args) + len(kwargs)


@pytest.mark.parametrize(
    ["func_to_check", "args", "kwargs", "expected_result"],
    [
        (sum_of_parameters, [1, 3, 5], {}, 9),
        (sum_of_parameters, [-1, 1, 3], {}, 3),
        (args_len_plus_kwargs_len, [7], {"a": 5, "b": "c", "d": "e"}, 4),
    ],
)
def test_cache_func(
    func_to_check: Callable, args: List[int], kwargs: Dict, expected_result: Any
):
    actual_result = cache(func_to_check)(*args, **kwargs)

    assert actual_result == expected_result
