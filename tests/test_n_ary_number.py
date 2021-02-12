# -*- coding: utf-8 -*-
import pytest

from snippets.math.n_ary_number import convert_decimal_to_n_ary_number


class TestNAryNumber:

    @pytest.mark.parametrize(('number', 'm_ary', 'expected'), [
        (0, 2, 0),
        (1, 2, 1),
        (2, 2, 10),
        (13, 2, 1101),
        (1, 3, 1),
        (2, 3, 2),
        (3, 3, 10),
        (4, 3, 11),
        (13, 3, 111),
        (10, 5, 20),
        (10, 6, 14),
        (10, 7, 13),
        (5191491411, 8, 46533757523),
        (10, 9, 11),
        (0, 9, 0),
        (334, 10, 334)
    ])
    def test_convert_decimal_to_n_ary_number(self, number, m_ary, expected):
        actual = convert_decimal_to_n_ary_number(number, m_ary)
        assert actual == expected
