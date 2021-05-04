# -*- coding: utf-8 -*-
import pytest

from snippets.dp.lcs import lcs


class TestLcs:
    @pytest.mark.parametrize(
        ("a", "b", "expected"),
        [
            (["a"], ["b"], 0),
            (["a", "b", "c"], ["a", "b", "c"], 3),
            (["a", "b", "c", "d"], ["b", "e", "c", "d"], 3),
            ([1], [2], 0),
            ([1, 2, 3], [1, 2, 3], 3),
            ([1, 3, 2, 4], [1, 5, 2, 6, 4, 3], 3),
            ([1, 2, 5, 4], [2, 3, 5, 1], 2),
        ],
    )
    def test_lcs(self, a, b, expected):
        actual = lcs(a, b)
        assert actual == expected
