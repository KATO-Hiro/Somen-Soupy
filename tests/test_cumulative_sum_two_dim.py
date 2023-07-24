# -*- coding: utf-8 -*-

from typing import List

import pytest

from snippets.technique.cumulative_sum_two_dim import CumulativeSum2d


@pytest.fixture
def array() -> List[List[int]]:
    return [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]


class TestCumulativeSum2d:
    @pytest.mark.parametrize(
        ("x1", "y1", "x2", "y2", "expected"),
        [
            (1, 1, 5, 3, 120),
            (1, 1, 3, 2, 27),
            (4, 2, 4, 3, 23),
            (5, 3, 5, 3, 15),
        ],
    )
    def test_cumulative_sum_2d(
        self, array: List[List[int]], x1: int, y1: int, x2: int, y2: int, expected: int
    ) -> None:
        c = CumulativeSum2d(array)
        actual = c.query(x1 - 1, y1 - 1, x2, y2)
        assert actual == expected

    @pytest.mark.parametrize(
        ("x1", "y1", "x2", "y2"),
        [
            (2, 1, 1, 1),
            (3, 2, 2, 1),
            (-1, 0, 5, 3),
            (0, -1, 5, 3),
            (-1, -1, 5, 3),
            (0, 0, 6, 3),
            (0, 0, 5, 4),
            (0, 0, 6, 4),
            (-1, -1, 6, 4),
        ],
    )
    def test_query_failed_if_invalid_input_is_given(
        self, array: List[List[int]], x1: int, y1: int, x2: int, y2: int
    ) -> None:
        c = CumulativeSum2d(array)

        with pytest.raises(AssertionError):
            c.query(x1, y1, x2, y2)
