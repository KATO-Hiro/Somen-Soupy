# -*- coding: utf-8 -*-
import pytest

from snippets.math.factorization import run_prime_factorization


class TestFactorization:

    @pytest.mark.parametrize(('number', 'expected'), [
        (1, {}),
        (2, {2: 1}),
        (3, {3: 1}),
        (4, {2: 2}),
        (5, {5: 1}),
        (11, {11: 1}),
        (12, {2: 2, 3: 1}),
        (600, {2: 3, 3: 1, 5: 2}),
        (10 ** 9 + 7, {10 ** 9 + 7: 1}),
        (10 ** 12, {2: 12, 5: 12}),
    ])
    def test_run_prime_factorization(self, number, expected):
        actual = run_prime_factorization(number)
        assert actual == expected
