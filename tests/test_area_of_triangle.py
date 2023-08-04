import pytest

from snippets.geometry.area_of_triangle import calc_area_of_triangle


class TestAreaOfTriangle:
    @pytest.mark.parametrize(
        ("point1", "point2", "point3", "expected"),
        [
            ((1, 1), (3, 4), (5, 1), 6.0),
            ((2, 2), (4, 4), (6, 6), 0.0),
        ],
    )
    def test_is_colinear(
        self, point1: tuple, point2: tuple, point3: tuple, expected: float
    ) -> None:
        actual = calc_area_of_triangle(point1, point2, point3)
        assert actual == expected
