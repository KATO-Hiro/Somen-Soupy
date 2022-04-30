# -*- coding: utf-8 -*-

import pytest

from snippets.math.combination import Combination


class TestFactorization:

    @pytest.mark.parametrize(('n', 'r', 'expected'), [
        (3, 1, 3),
        (3, 2, 3),
        (5, 3, 10),
        (5, 5, 1),
        (5, 0, 1),
        (3, 4, 0),
        (3, 5, 0),
        (-1, 5, 0),
        (-1, -1, 0),
        (2, -1, 0),
        (47, 5, 1533939),
        (47, 10, 178066716),
        (10 ** 5, 99998, 999949972),
        (10 ** 5, 10 ** 5, 1),
        (10 ** 5, 1, 10 ** 5),
        (3 + 4 - 1, 4, 15),
    ])
    def test_count_combination(self, n, r, expected):
        combination = Combination(max_value=10 ** 5 + 100)
        actual = combination.count_nCr(n, r)
        assert actual == expected

    def test_count_combination_using_original_mod(self):
        mod = 998244353
        combination = Combination(max_value=10 ** 5 + 100, mod=mod)
        actual = combination.count_nCr(90081, 48090) * combination.count_nCr(90081, 52771)
        actual = actual % mod
        assert actual == 577742975
    
    @pytest.mark.parametrize(('n', 'r', 'expected'), [
        (1, 4, 1),
        (3, 4, 15),
        (0, 4, 0),
        (-1, 4, 0),
        (4, -1, 0),
    ])
    def test_count_nHr(self, n: int, r: int, expected: int) -> None:
        combination = Combination(max_value=10 ** 5 + 100)
        actual = combination.count_nHr(n, r)
        assert actual == expected
