# -*- coding: utf-8 -*-
import pytest

from snippets.math.comress import compress_coordinate


class TestFactorization:

    @pytest.mark.parametrize(('numbers', 'expected'), [
        ([10000000], {10000000: 0}),
        ([3, 3, 1, 6, 1], {1: 0, 3: 1, 6: 2}),
        ([1000, 10000, 1, 10, 100], {1: 0, 10: 1, 100: 2, 1000: 3, 10000: 4}),
    ])
    def test_comress(self, numbers, expected):
        actual = compress_coordinate(numbers)
        assert actual == expected
