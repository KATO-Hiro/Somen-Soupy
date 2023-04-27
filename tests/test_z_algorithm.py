# -*- coding: utf-8 -*-

from typing import List
import pytest

from snippets.string.z_algorithm import z_algorithm


class TestZAlgorithm:

    @pytest.mark.parametrize(('s', 'expected'), [
        ("abababab", [8, 0, 6, 0, 4, 0, 2, 0]),
        ("agccga", [6, 0, 0, 0, 0, 1]),
    ])
    def test_z_algorithm(self, s: str, expected: List[int]) -> None:
        actual = z_algorithm(s)
        assert actual == expected
