# -*- coding: utf-8 -*-
import pytest

from snippets.math.combination import count_combination


class TestFactorization(object):

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
        actual = count_combination(n, r)
        assert actual == expected

    def test_count_combination_using_original_mod(self):
        mod = 998244353
        actual = count_combination(90081, 48090, mod) * count_combination(90081, 52771, mod)
        actual = actual % mod
        assert actual == 577742975
