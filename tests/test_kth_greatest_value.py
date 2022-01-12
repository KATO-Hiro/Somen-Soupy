import pytest

from snippets.data_structure.kth_greatest_value import get_kth_greatest_value


class TestLcm:
    @pytest.mark.parametrize(
        ("array", "k", "expected"),
        [
            ([1, 2, 3], 2, [1, 2]),
            ([3, 7, 2, 5, 11, 6, 1, 9, 8, 10, 4], 5, [2, 3, 3, 5, 6, 7, 7]),
        ],
    )
    def test_get_kth_greatest_value(self, array, k, expected):
        actual = get_kth_greatest_value(array, k)
        assert actual == expected
