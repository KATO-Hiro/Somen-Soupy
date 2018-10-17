# -*- coding: utf-8 -*-
import pytest

from snippets.prime import Prime


class TestPrime(object):

    @pytest.mark.parametrize(('number', 'expected'), [
        (-1.1, False),
        (-1, False),
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (3.0, False),
        (3.1, False),
        (4, False),
        (5, True),
        (11, True),
        (10 ** 9 + 7, True),
    ])
    def test_is_prime(self, number, expected):
        prime = Prime(number)
        actual = prime.is_included()
        assert actual == expected
