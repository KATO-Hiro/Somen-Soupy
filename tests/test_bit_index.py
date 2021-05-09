from typing import List
import pytest

from snippets.math.bit_index import get_bit_index


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (0, []),
        (1, [1]),
        (2, [2]),
        (3, [1, 2]),
        (4, [3]),
        (5, [1, 3]),
        (6, [2, 3]),
        (7, [1, 2, 3]),
        (8, [4]),
    ],
)
def test_get_bit_index(number: int, expected: List[int]) -> None:
    actual = get_bit_index(number)

    assert actual == expected
