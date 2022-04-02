# -*- coding: utf-8 -*-

import pytest

from snippets.string.run_length import run_length_encoding
from snippets.string.run_length import run_length_decoding


class TestRunLength:
    @pytest.mark.parametrize(
        ("s", "expected"),
        [
            (["a", "a", "a", "b", "c", "c", "c", "c", "d", "d"],
                [["a", 3], ["b", 1], ["c", 4], ["d", 2]]),
            (["b", "b", "b", "a", "c", "c", "c", "c", "d", "d"],
                [["b", 3], ["a", 1], ["c", 4], ["d", 2]]),
            ([0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 5],
                [[0, 3], [1, 3], [2, 4], [3, 2], [4, 1], [5, 2]]),

        ],
    )
    def test_run_length_encoding(self, s, expected):
        actual = run_length_encoding(s)
        assert actual == expected

    @pytest.mark.parametrize(
        ("s", "expected"),
        [
            ([["a", 3], ["b", 1], ["c", 4], ["d", 2]],
                "aaabccccdd"),
            ([["b", 3], ["a", 1], ["c", 4], ["d", 2]],
                "bbbaccccdd"),
            ([[0, 3], [1, 3], [2, 4], [3, 2], [4, 1], [5, 2]],
                "000111222233455"),

        ],
    )
    def test_run_length_decoding(self, s, expected):
        actual = run_length_decoding(s)
        assert actual == expected
