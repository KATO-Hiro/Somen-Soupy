# -*- coding: utf-8 -*-
import pytest

from snippets.math.lcm import lcm


class TestLcm:

    @pytest.mark.parametrize(('a', 'b', 'expected'), [
        (1, 1, 1),
        (2, 3, 6),
        (12, 4, 12),
        (4, 12, 12),
    ])
    def test_lcm(self, a, b, expected):
        actual = lcm(a, b)
        assert actual == expected
