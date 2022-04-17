import pytest

from snippets.geometry.is_colinear import is_colinear


class TestIsColinear:
    @pytest.mark.parametrize(
        ("point", "point1", "point2", "expected"),
        [
            ((1, 3), (0, 0), (2, 6), True),
            ((0.5, 1.5), (0, 0), (2, 6), True),
            ((1.5, 4.5), (0, 0), (2, 6), True),
            ((0, 0), (0, 0), (2, 6), True),
            ((2, 6), (0, 0), (2, 6), True),
            ((1, 2), (0, 0), (2, 6), False),
            ((1, 4), (0, 0), (2, 6), False),
            ((1, 1), (0, 0), (4, 4), True),
            ((2, 2), (0, 0), (4, 4), True),
            ((3, 3), (0, 0), (4, 4), True),
            ((1, 0), (0, 0), (4, 4), False),
            ((1, 2), (0, 0), (4, 4), False),
            ((2, 1), (0, 0), (4, 4), False),
            ((2, 3), (0, 0), (4, 4), False),
        ],
    )
    def test_is_colinear(
            self,
            point: tuple,
            point1: tuple,
            point2: tuple,
            expected: bool
            ) -> None:
        actual = is_colinear(point, point1, point2)
        assert actual == expected
