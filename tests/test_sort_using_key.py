# -*- coding: utf-8 -*-

from typing import List, Tuple

import pytest

from snippets.math.sort_using_key import Fraction, compare


class TestSortByKey:
    @pytest.mark.parametrize(
        ("a", "b", "expected"),
        [
            ([1, 3, 2, 1, 3], [3, 1, 2, 2, 6], [2, 3, 4, 5, 1]),
            ([433494437, 165580141], [701408733, 267914296], [2, 1]),
        ],
    )
    def test_fraction(self, a: List[int], b: List[int], expected: List[int]) -> None:
        n = len(a)

        # Sort id based on ai / (ai + bi)
        actual = sorted(
            range(1, n + 1),
            key=lambda i: Fraction(a[i - 1], a[i - 1] + b[i - 1]),
            reverse=True,
        )
        assert actual == expected

    @pytest.mark.parametrize(
        ("ab", "expected"),
        [
            ([(1, 3, 1), (3, 1, 2), (2, 2, 3), (1, 2, 4), (3, 6, 5)], [2, 3, 4, 5, 1]),
            ([(433494437, 701408733, 1), (165580141, 267914296, 2)], [2, 1]),
        ],
    )
    def test_compare(self, ab: List[Tuple[int, int, int]], expected: List[int]) -> None:
        from functools import cmp_to_key

        # Sort id based on ai / (ai + bi)
        tmp = sorted(ab, key=cmp_to_key(compare), reverse=True)
        actual = list()

        for _, _, i in tmp:
            actual.append(i)

        assert actual == expected
