# -*- coding: utf-8 -*-


import pytest

from snippets.data_structure.sorted_set import SortedSet


@pytest.fixture
def sortedset() -> SortedSet:
    return SortedSet()


@pytest.fixture
def sortedset_with_values() -> SortedSet:
    return SortedSet([3, 1, 4, 15, 9, 2, 6, 53, 58, 97, 93, 23, 8, 46])


class TestSortedSet:

    def test_add(self, sortedset: SortedSet) -> None:
        assert sortedset.a == []
        assert len(sortedset.a) == 0

        expected = [[[1]], [[1, 2]], [[1, 2, 3]]]

        for i in range(1, 3 + 1):
            sortedset.add(i)  # type: ignore
            assert sortedset.a == expected[i - 1]  # 0-indexed.

            assert len(sortedset.a) == 1
            assert len(sortedset.a[0]) == i

    def test_discard(self, sortedset: SortedSet) -> None:
        assert sortedset.a == []

        expected = [[[1]], [[1, 2]], [[1, 2, 3]]]

        for i in range(1, 3 + 1):
            sortedset.add(i)  # type: ignore
            assert sortedset.a == expected[i - 1]  # 0-indexed.

        sortedset.discard(2)  # type: ignore
        assert sortedset.a == [[1, 3]]
        assert len(sortedset.a[0]) == 2

        sortedset.discard(2)  # type: ignore
        assert sortedset.a == [[1, 3]]
        assert len(sortedset.a[0]) == 2

        sortedset.discard(4)  # type: ignore
        assert sortedset.a == [[1, 3]]
        assert len(sortedset.a[0]) == 2

        sortedset.discard(0)  # type: ignore
        assert sortedset.a == [[1, 3]]
        assert len(sortedset.a[0]) == 2

        sortedset.discard(1)  # type: ignore
        assert sortedset.a == [[3]]
        assert len(sortedset.a[0]) == 1

        sortedset.discard(3)  # type: ignore
        assert sortedset.a == []
        assert len(sortedset.a) == 0

    @pytest.mark.parametrize(('base', 'expected'), [
        (10, 9),
        (2, 1),
        (1, None),
        (100, 97),
        (98, 97),
        (97, 93),
    ])
    def test_lt(
            self,
            sortedset_with_values: SortedSet,
            base: int,
            expected: int
            ) -> None:
        actual = sortedset_with_values.lt(base)  # type: ignore
        assert actual == expected

    @pytest.mark.parametrize(('base', 'expected'), [
        (10, 9),
        (2, 2),
        (1, 1),
        (0, None),
        (100, 97),
        (98, 97),
        (97, 97),
    ])
    def test_le(
            self,
            sortedset_with_values: SortedSet,
            base: int,
            expected: int
            ) -> None:
        actual = sortedset_with_values.le(base)  # type: ignore
        assert actual == expected

    @pytest.mark.parametrize(('base', 'expected'), [
        (10, 15),
        (2, 3),
        (1, 2),
        (0, 1),
        (100, None),
        (97, None),
        (96, 97),
    ])
    def test_gt(
            self,
            sortedset_with_values: SortedSet,
            base: int,
            expected: int
            ) -> None:
        actual = sortedset_with_values.gt(base)  # type: ignore
        assert actual == expected

    @pytest.mark.parametrize(('base', 'expected'), [
        (10, 15),
        (2, 2),
        (1, 1),
        (0, 1),
        (100, None),
        (98, None),
        (97, 97),
        (96, 97),
    ])
    def test_ge(
            self,
            sortedset_with_values: SortedSet,
            base: int,
            expected: int
            ) -> None:
        actual = sortedset_with_values.ge(base)  # type: ignore
        assert actual == expected

    @pytest.mark.parametrize('x', [
        1,
        2,
        3,
        93,
        97,
    ])
    def test_exists_element(
            self,
            sortedset_with_values: SortedSet,
            x: int
            ) -> None:
        assert x in sortedset_with_values  # type: ignore

    @pytest.mark.parametrize('x', [
        -1,
        0,
        100,
    ])
    def test_not_exists_element(
            self,
            sortedset_with_values: SortedSet,
            x: int
            ) -> None:
        assert x not in sortedset_with_values  # type: ignore

    @pytest.mark.parametrize(('x', 'expected'), [
        (0, 1),
        (1, 2),
        (12, 93),
        (13, 97),
    ])
    def test_xth_element_from_min_value(
            self,
            sortedset_with_values: SortedSet,
            x: int,
            expected: int
            ) -> None:
        assert sortedset_with_values[x] == expected  # 0-indexed.

    @pytest.mark.parametrize(('x', 'expected'), [
        (0, 97),
        (1, 93),
        (12, 2),
        (13, 1),
    ])
    def test_xth_element_from_max_value(
            self,
            sortedset_with_values: SortedSet,
            x: int,
            expected: int
            ) -> None:
        assert sortedset_with_values[~x] == expected  # 0-indexed.

    @pytest.mark.parametrize(('base', 'expected'), [
        (0, 0),
        (1, 0),
        (2, 1),
        (96, 13),
        (97, 13),
        (98, 14),
        (100, 14),
    ])
    def test_index(
            self,
            sortedset_with_values: SortedSet,
            base: int,
            expected: int
            ) -> None:
        actual = sortedset_with_values.index(base)  # type: ignore
        assert actual == expected

    @pytest.mark.parametrize(('base', 'expected'), [
        (0, 0),
        (1, 1),
        (2, 2),
        (96, 13),
        (97, 14),
        (98, 14),
    ])
    def test_index_right(
            self,
            sortedset_with_values: SortedSet,
            base: int,
            expected: int
            ) -> None:
        actual = sortedset_with_values.index_right(base)  # type: ignore
        assert actual == expected
