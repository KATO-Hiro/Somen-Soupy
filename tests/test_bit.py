# -*- coding: utf-8 -*-

from typing import List
import pytest

from snippets.data_structure.bit import calc_inversion_number


class TestBIT:

    @pytest.mark.parametrize(('a', 'expected'), [
        ([3, 10, 1, 8, 5], 5),
        ([1, 2, 3, 4, 5], 0),
        ([1, 2, 3, 3, 5, 5], 0),
        ([-1, -1, 2, 3, 3, 5, 5], 0),
    ])
    def test_calc_inversion_number(self, a: List[int], expected: int):
        actual = calc_inversion_number(a)
        assert actual == expected
