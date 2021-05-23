import pytest

from snippets.math.pascals_triangle import calc_pascals_triangle


class TestNAryNumber:
    @pytest.mark.parametrize(
        ("n_max", "expected"),
        [
            (1, [[1, 0], [1, 1]]),
            (2, [[1, 0, 0], [1, 1, 0], [1, 2, 1]]),
            (3, [[1, 0, 0, 0], [1, 1, 0, 0], [1, 2, 1, 0], [1, 3, 3, 1]]),
            (
                4,
                [
                    [1, 0, 0, 0, 0],
                    [1, 1, 0, 0, 0],
                    [1, 2, 1, 0, 0],
                    [1, 3, 3, 1, 0],
                    [1, 4, 6, 4, 1],
                ],
            ),
            (
                5,
                [
                    [1, 0, 0, 0, 0, 0],
                    [1, 1, 0, 0, 0, 0],
                    [1, 2, 1, 0, 0, 0],
                    [1, 3, 3, 1, 0, 0],
                    [1, 4, 6, 4, 1, 0],
                    [1, 5, 10, 10, 5, 1],
                ],
            ),
            (
                6,
                [
                    [1, 0, 0, 0, 0, 0, 0],
                    [1, 1, 0, 0, 0, 0, 0],
                    [1, 2, 1, 0, 0, 0, 0],
                    [1, 3, 3, 1, 0, 0, 0],
                    [1, 4, 6, 4, 1, 0, 0],
                    [1, 5, 10, 10, 5, 1, 0],
                    [1, 6, 15, 20, 15, 6, 1],
                ],
            ),
        ],
    )
    def test_calc_pascals_triangle(self, n_max, expected):
        actual = calc_pascals_triangle(n_max)
        assert actual == expected
