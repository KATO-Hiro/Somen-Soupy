# -*- coding: utf-8 -*-
import pytest

from snippets.prime import Prime


class TestPrime:

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

    @pytest.mark.parametrize(('number', 'expected'), [
        (1, []),
        (2, [2]),
        (3, [2, 3]),
        (11, [2, 3, 5, 7, 11]),
    ])
    def test_generate(self, number, expected):
        prime = Prime(number)
        actual = prime.generate()
        assert actual == expected

    @pytest.mark.parametrize(('number', 'expected'), [
        (1, []),
        (2, [2]),
        (3, [2, 3]),
        (11, [2, 3, 5, 7, 11]),
    ])
    def test_generate_twice(self, number, expected):
        prime = Prime(number)
        actual = prime.generate()
        actual = prime.generate()
        assert actual == expected
