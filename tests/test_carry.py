# -*- coding: utf-8 -*-

from typing import List
import pytest

from snippets.math.carry import carry


class TestDigit:

    @pytest.mark.parametrize(('n', 'digits', 'expected'), [
        (3, [0, 1, 2], [1, 2]),
        (3, [0, 1, 11], [2, 1]),
        (3, [0, 9, 11], [1, 0, 1]),
        (3, [0, 10, 11], [1, 1, 1]),
        (3, [0, 10000, 11], [1000, 1, 1]),
        (10, [0, 9, 11, 4, 15, 119, 2, 36, 7, 8, 9], [1, 0, 1, 6, 6, 9, 5, 6, 7, 8, 9]),
    ])
    def test_carry(self, n: int, digits: List[int], expected: List[int]):
        actual = carry(n, digits)
        assert actual == expected
