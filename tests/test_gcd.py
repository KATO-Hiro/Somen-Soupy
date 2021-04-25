import pytest

from snippets.math.gcd import extgcd


class TestLcm:
    @pytest.mark.parametrize(
        ("a", "b", "expected"),
        [
            (111, 30, (3, 3, -11)),
            (0, 0, (0, 1, 0)),
            (1, 0, (1, 1, 0)),
        ],
    )
    def test_gcd(self, a, b, expected):
        actual = extgcd(a, b)
        assert actual == expected
