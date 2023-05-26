# -*- coding: utf-8 -*-


from typing import List, Tuple

import pytest

from snippets.technique.bisect_wrapper import bisect_ge, bisect_gt, bisect_le, bisect_lt


class TestBisectWrapper:
    @pytest.mark.parametrize(
        ("sorted_array", "value", "expected"),
        [
            ([1, 2, 3, 10, 11], -1, (None, None)),
            ([1, 2, 3, 10, 11], 0, (None, None)),
            ([1, 2, 3, 10, 11], 1, (None, None)),
            ([1, 2, 3, 10, 11], 2, (0, 1)),
            ([1, 2, 3, 10, 11], 3, (1, 2)),
            ([1, 2, 3, 10, 11], 4, (2, 3)),
            ([1, 2, 3, 10, 11], 7, (2, 3)),
            ([1, 2, 3, 10, 11], 10, (2, 3)),
            ([1, 2, 3, 10, 11], 12, (4, 11)),
            ([1, 2, 3, 10, 11], 15, (4, 11)),
        ],
    )
    def test_bisect_lt(
        self,
        sorted_array: List[int],
        value: int,
        expected,
    ) -> None:
        actual_id, actual_value = bisect_lt(sorted_array, value)
        expected_id, expected_value = expected

        assert actual_id == expected_id
        assert actual_value == expected_value

    @pytest.mark.parametrize(
        ("sorted_array", "value", "expected"),
        [
            ([1, 2, 3, 10, 11], -1, (None, None)),
            ([1, 2, 3, 10, 11], 0, (None, None)),
            ([1, 2, 3, 10, 11], 1, (0, 1)),
            ([1, 2, 3, 10, 11], 2, (1, 2)),
            ([1, 2, 3, 10, 11], 3, (2, 3)),
            ([1, 2, 3, 10, 11], 4, (2, 3)),
            ([1, 2, 3, 10, 11], 7, (2, 3)),
            ([1, 2, 3, 10, 11], 10, (3, 10)),
            ([1, 2, 3, 10, 11], 12, (4, 11)),
            ([1, 2, 3, 10, 11], 15, (4, 11)),
        ],
    )
    def test_bisect_le(
        self,
        sorted_array: List[int],
        value: int,
        expected,
    ) -> None:
        actual_id, actual_value = bisect_le(sorted_array, value)
        expected_id, expected_value = expected

        assert actual_id == expected_id
        assert actual_value == expected_value

    @pytest.mark.parametrize(
        ("sorted_array", "value", "expected"),
        [
            ([-10, -5, -2, -1, 0, 1, 2, 3, 10], -11, (0, -10)),
            ([-10, -5, -2, -1, 0, 1, 2, 3, 10], -10, (1, -5)),
            ([-10, -5, -2, -1, 0, 1, 2, 3, 10], -5, (2, -2)),
            ([-10, -5, -2, -1, 0, 1, 2, 3, 10], -3, (2, -2)),
            ([-10, -5, -2, -1, 0, 1, 2, 3, 10], -1, (4, 0)),
            ([-10, -5, -2, -1, 0, 1, 2, 3, 10], 2, (7, 3)),
            ([-10, -5, -2, -1, 0, 1, 2, 3, 10], 5, (8, 10)),
            ([-10, -5, -2, -1, 0, 1, 2, 3, 10], 6, (8, 10)),
            ([-10, -5, -2, -1, 0, 1, 2, 3, 10], 9, (8, 10)),
            ([-10, -5, -2, -1, 0, 1, 2, 3, 10], 10, (None, None)),
            ([-10, -5, -2, -1, 0, 1, 2, 3, 10], 11, (None, None)),
        ],
    )
    def test_bisect_gt(
        self,
        sorted_array: List[int],
        value: int,
        expected,
    ) -> None:
        actual_id, actual_value = bisect_gt(sorted_array, value)
        expected_id, expected_value = expected

        assert actual_id == expected_id
        assert actual_value == expected_value

    @pytest.mark.parametrize(
        ("sorted_array", "value", "expected"),
        [
            ([-10, -5, -2, -1, 0, 1, 2, 3, 10], -11, (0, -10)),
            ([-10, -5, -2, -1, 0, 1, 2, 3, 10], -10, (0, -10)),
            ([-10, -5, -2, -1, 0, 1, 2, 3, 10], -9, (1, -5)),
            ([-10, -5, -2, -1, 0, 1, 2, 3, 10], -5, (1, -5)),
            ([-10, -5, -2, -1, 0, 1, 2, 3, 10], -3, (2, -2)),
            ([-10, -5, -2, -1, 0, 1, 2, 3, 10], -1, (3, -1)),
            ([-10, -5, -2, -1, 0, 1, 2, 3, 10], 2, (6, 2)),
            ([-10, -5, -2, -1, 0, 1, 2, 3, 10], 3, (7, 3)),
            ([-10, -5, -2, -1, 0, 1, 2, 3, 10], 5, (8, 10)),
            ([-10, -5, -2, -1, 0, 1, 2, 3, 10], 9, (8, 10)),
            ([-10, -5, -2, -1, 0, 1, 2, 3, 10], 10, (8, 10)),
            ([-10, -5, -2, -1, 0, 1, 2, 3, 10], 11, (None, None)),
        ],
    )
    def test_bisect_ge(
        self,
        sorted_array: List[int],
        value: int,
        expected,
    ) -> None:
        actual_id, actual_value = bisect_ge(sorted_array, value)
        expected_id, expected_value = expected

        assert actual_id == expected_id
        assert actual_value == expected_value
