# -*- coding: utf-8 -*-

import pytest

from snippets.math.permutation import Permutation


class TestFactorization:
    @pytest.mark.parametrize(
        ("n", "r", "expected"),
        [
            (-1, -1, 0),
            (-1, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 1, 0),
            (1, 1, 1),
            (7, 1, 7),
            (7, 3, 210),
            (7, 5, 2520),
            (7, 7, 5040),
            (7, 8, 0),
            (15, 2, 210),
            (15, 15, 674358851),
            (10 ** 5, 1, 10 ** 5),
            (10 ** 5, 2, 999899937),
        ],
    )
    def test_count_permutation(self, n, r, expected):
        permutation = Permutation(max_value=10 ** 5 + 100)
        actual = permutation.count_nPr(n, r)
        assert actual == expected
