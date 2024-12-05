from typing import Any, Callable, List, Tuple

import pytest

from lecture_03_functional_programming.hw.tasks.task01 import cache


def func_for_the_test(a, b, c):
    return a + b + c


def args_len_plus_kwargs_len(*args, **kwargs):
    return len(args) + len(kwargs)


@pytest.mark.parametrize(
    ["func_to_check", "times", "values", "expected_result"],
    [
        (func_for_the_test, 1, ([1, 3, 5], [1, 3, 5]), 9),
        (func_for_the_test, 1, ([-1, 1, 3], [-1, 1, 3]), 3),
    ],
)
def test_cache_func(
    func_to_check: Callable, times: int, values: Tuple[List], expected_result: Any
):
    cache_func = cache(times)(func_to_check)
    actual_result = cache_func(*values[0])
    actual_result2 = cache_func(*values[1])

    assert actual_result == actual_result2 == expected_result


@pytest.mark.parametrize(
    ["func_to_check", "times", "values", "expected_result"],
    [
        (args_len_plus_kwargs_len, 1, {"a": 5, "b": "c", "d": "e"}, 3),
        (args_len_plus_kwargs_len, 1, {"e": 3}, 1),
    ],
)
def test_cache_func_with_kwargs(
    func_to_check: Callable, times: int, values: Tuple[List], expected_result: Any
):
    cache_func = cache(times)(func_to_check)
    actual_result = cache_func(**values)

    assert actual_result == expected_result
