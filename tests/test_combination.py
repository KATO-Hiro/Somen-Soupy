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
        (47, 5, 1533939),
        (47, 10, 178066716),
        (10 ** 5, 99998, 999949972),
        (10 ** 5, 10 ** 5, 1),
        (10 ** 5, 1, 10 ** 5),
    ])
    def test_count_combination(self, n, r, expected):
        actual = count_combination(n, r)
        assert actual == expected
