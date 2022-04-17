import pytest

from snippets.geometry.line_passing_through_points import calc_line_passing_through


class TestIsColinear:
    @pytest.mark.parametrize(
        ("point1", "point2", "expected"),
        [
            ((0, 0), (2, 6), (3, -1, 0)),
            ((1, 0), (2, 0), (0, 1, 0)),
            ((0, 1), (3, 4), (1, -1, 1)),
            ((3, 4), (0, 1), (1, -1, 1)),
        ],
    )
    def test_is_colinear(
            self,
            point1: tuple,
            point2: tuple,
            expected: bool
            ) -> None:
        actual = calc_line_passing_through(point1, point2)
        assert actual == expected
