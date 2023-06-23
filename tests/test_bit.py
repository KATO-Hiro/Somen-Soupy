# -*- coding: utf-8 -*-

from typing import List, Tuple

import pytest

from snippets.data_structure.bit import BIT, calc_inversion_number


@pytest.fixture
def bit() -> BIT:
    return BIT(8)


@pytest.fixture
def a() -> List[int]:
    return [3, 1, 4, 1, 5, 9, 2, 6]


class TestBIT:
    def test_initial_status(self, bit: BIT) -> None:
        assert bit.tree == [0] * (8 + 1)  # 0-indexed

        pair_of_positions = self._generate_pair_of_positions()

        for left, right in pair_of_positions:
            assert bit.range_sum(left, right) == 0

    def _generate_pair_of_positions(self) -> List[Tuple[int, ...]]:
        from itertools import combinations_with_replacement

        return list(combinations_with_replacement(range(8 + 1), 2))

    def test_add(self, bit: BIT) -> None:
        bit.add(0, 1)
        assert bit.tree == [0, 1, 1, 0, 1, 0, 0, 0, 1]

    def test_add_multiple_times(self, bit: BIT) -> None:
        expected = [
            [0, 1, 1, 0, 1, 0, 0, 0, 1],
            [0, 1, 3, 0, 3, 0, 0, 0, 3],
            [0, 1, 3, 3, 6, 0, 0, 0, 6],
            [0, 1, 3, 3, 10, 0, 0, 0, 10],
            [0, 1, 3, 3, 10, 5, 5, 0, 15],
            [0, 1, 3, 3, 10, 5, 11, 0, 21],
            [0, 1, 3, 3, 10, 5, 11, 7, 28],
            [0, 1, 3, 3, 10, 5, 11, 7, 36],
        ]

        for i in range(8):
            bit.add(i, i + 1)
            assert bit.tree == expected[i]

    def test_add_when_negative_value_is_given(self, bit: BIT) -> None:
        for i in range(8):
            bit.add(i, i + 1)

        assert bit.tree == [0, 1, 3, 3, 10, 5, 11, 7, 36]

        bit.add(0, -5)
        assert bit.tree == [0, -4, -2, 3, 5, 5, 11, 7, 31]

    def test_add_when_zero_is_given(self, bit: BIT) -> None:
        for i in range(8):
            bit.add(i, i + 1)

        assert bit.tree == [0, 1, 3, 3, 10, 5, 11, 7, 36]

        bit.add(0, 0)
        assert bit.tree == [0, 1, 3, 3, 10, 5, 11, 7, 36]

    def test_add_when_positive_floating_point_value_is_given(self, bit: BIT) -> None:
        bit.add(0, 1.5)
        assert bit.tree == [0, 1.5, 1.5, 0, 1.5, 0, 0, 0, 1.5]

    def test_add_when_negative_floating_point_value_is_given(self, bit: BIT) -> None:
        bit.add(0, -1.5)
        assert bit.tree == [0, -1.5, -1.5, 0, -1.5, 0, 0, 0, -1.5]

    def test_get(self, bit: BIT, a: List[int]) -> None:
        for index, ai in enumerate(a):
            bit.add(index, ai)

        for index, ai in enumerate(a):
            assert bit.get(index) == ai

    @pytest.mark.parametrize(
        ("left", "right", "expected"),
        [
            (0, 8, 36),
            (0, 7, 28),
            (1, 7, 27),
            (1, 3, 5),
            (2, 2, 0),
        ],
    )
    def test_range_sum(self, bit: BIT, left: int, right: int, expected: int) -> None:
        for i in range(8):
            bit.add(i, i + 1)

        assert bit.range_sum(left, right) == expected

    @pytest.mark.parametrize(
        ("left", "right", "expected"),
        [
            (0, 8, 38),
            (0, 7, 30),
            (0, 2, 3),
            (0, 1, 1),
            (1, 4, 11),
            (1, 3, 7),
            (2, 2, 0),
        ],
    )
    def test_range_sum_when_additional_element_is_given(
        self, bit: BIT, left: int, right: int, expected: int
    ) -> None:
        for i in range(8):
            bit.add(i, i + 1)

        assert bit.range_sum(0, 8) == 36

        bit.add(2, 2)
        bit.tree = [0, 1, 5, 3, 12, 5, 11, 7, 38]

    @pytest.mark.parametrize(
        ("value", "expected"),
        [
            (0, 0),
            (1, 0),
            (2, 1),
            (3, 1),
            (4, 2),
            (6, 2),
            (36, 7),
            (37, 8),
            (38, 8),
        ],
    )
    def test_lower_bound(self, bit: BIT, value: int, expected: int) -> None:
        for i in range(8):
            bit.add(i, i + 1)

        assert bit.lower_bound(value) == expected

    @pytest.mark.parametrize(
        ("index"),
        [
            -2,
            -1,
            8,
            9,
        ],
    )
    def test_add_failed_if_invalid_input_is_given(self, bit: BIT, index: int) -> None:
        with pytest.raises(AssertionError):
            bit.add(index, None)

    @pytest.mark.parametrize(
        ("left", "right"),
        [
            (-2, 8),
            (-1, 8),
            (0, 9),
            (0, 10),
            (3, 2),
            (-1, 8),
            (-1, 9),
        ],
    )
    def test_range_sum_failed_if_invalid_input_is_given(
        self, bit: BIT, left: int, right: int
    ) -> None:
        with pytest.raises(AssertionError):
            bit.range_sum(left, right)

    @pytest.mark.parametrize(
        ("a", "expected"),
        [
            ([3, 10, 1, 8, 5], 5),
            ([1, 2, 3, 4, 5], 0),
            ([1, 2, 3, 3, 5, 5], 0),
            ([-1, -1, 2, 3, 3, 5, 5], 0),
        ],
    )
    def test_calc_inversion_number(self, a: List[int], expected: int) -> None:
        actual = calc_inversion_number(a)
        assert actual == expected
