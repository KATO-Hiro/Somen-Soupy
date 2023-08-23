# -*- coding: utf-8 -*-

import pytest

from snippets.geometry.two_circles_position import (
    TwoCirclesPosition,
    is_hit,
    is_intersected,
    is_on_circle,
)


class TestTwoCirclesPosition:
    @pytest.mark.parametrize(
        ("xi", "yi", "ri", "x", "y", "expected"),
        [
            (1, 1, 2, 3, 1, True),
            (1, 1, 2, -1, 1, True),
            (1, 1, 2, 1, 3, True),
            (1, 1, 2, 1, -1, True),
            (1, 1, 2, 3, 2, False),
        ],
    )
    def test_is_on_circle(
        self, xi: int, yi: int, ri: int, x: int, y: int, expected: bool
    ) -> None:
        actual = is_on_circle(xi, yi, ri, x, y)
        assert actual == expected

    @pytest.mark.parametrize(
        ("xi", "yi", "ri", "xj", "yj", "rj", "expected"),
        [
            (0, 0, 1, 1, 2, 2, True),
            (0, 0, 2, 4, 0, 2, True),
            (0, 0, 2, 1, 0, 1, True),
            (0, 0, 2, 0, 0, 1, False),
            (0, 0, 1, 3, 0, 1, False),
        ],
    )
    def test_is_hit(
        self, xi: int, yi: int, ri: int, xj: int, yj: int, rj: int, expected: bool
    ) -> None:
        actual = is_hit(xi, yi, ri, xj, yj, rj)
        assert actual == expected

    @pytest.mark.parametrize(
        ("xi", "yi", "ri", "xj", "yj", "rj", "expected"),
        [
            (0, 0, 1, 1, 2, 2, TwoCirclesPosition.Intersect),
            (0, 0, 2, 4, 0, 2, TwoCirclesPosition.Circumscribed),
            (0, 0, 2, 1, 0, 1, TwoCirclesPosition.Inscribed),
            (0, 0, 2, 0, 0, 1, TwoCirclesPosition.Inside),
            (0, 0, 1, 3, 0, 1, TwoCirclesPosition.Outside),
            (5, 5, 3, 5, 5, 3, TwoCirclesPosition.Inscribed),
        ],
    )
    def test_is_intersected(
        self, xi: int, yi: int, ri: int, xj: int, yj: int, rj: int, expected
    ) -> None:
        actual = is_intersected(xi, yi, ri, xj, yj, rj)
        assert actual == expected
