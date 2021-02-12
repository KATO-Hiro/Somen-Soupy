# -*- coding: utf-8 -*-
import pytest

from snippets.math.digit import count_digit


class TestDigit:

    @pytest.mark.parametrize(('number', 'expected'), [
        (0, 1),
        (1, 1),
        (2, 1),
        (10, 2),
        (11, 2),
        (99, 2),
        (100, 3),
        (10 ** 9 + 7, 10),
    ])
    def test_run_prime_factorization(self, number, expected):
        actual = count_digit(number)
        assert actual == expected
