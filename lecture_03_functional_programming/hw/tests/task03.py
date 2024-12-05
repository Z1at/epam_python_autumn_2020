from typing import Dict, List

import pytest

from lecture_03_functional_programming.hw.tasks.task03 import make_filter


@pytest.mark.parametrize(
    ["keywords", "data", "expected_result"],
    [
        (
            {"color": "blue", "height": 6},
            [
                {"color": "yellow", "height": 7, "width": 3},
                {"color": "blue", "height": 5},
            ],
            [],
        ),
        (
            {"color": "blue", "height": 6},
            [
                {"color": "blue", "height": 6, "width": 3},
                {"color": "blue", "height": 5},
            ],
            [{"color": "blue", "height": 6, "width": 3}],
        ),
        (
            {"color": "blue", "height": 6},
            [
                {"color": "blue", "height": 6, "width": 3},
                {"color": "blue", "height": 6},
            ],
            [
                {"color": "blue", "height": 6, "width": 3},
                {"color": "blue", "height": 6},
            ],
        ),
    ],
)
def test_make_filter(keywords: Dict, data: Dict, expected_result: List):
    actual_result = make_filter(**keywords).apply(data)

    assert actual_result == expected_result
