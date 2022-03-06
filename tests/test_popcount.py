# -*- coding: utf-8 -*-


import pytest

from snippets.string.popcount import popcount


class TestPopcount:
    @pytest.mark.parametrize(
        ("n", "expected"),
        [
            (0, 0),
            (1, 1),
            (2, 1),
            (3, 2),
            (10, 2),
            (100, 3),
        ],
    )
    def test_popcount(self, n, expected):
        actual = popcount(n)
        assert actual == expected
