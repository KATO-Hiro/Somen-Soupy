# -*- coding: utf-8 -*-


import pytest

from snippets.data_structure.sorted_multi_set import SortedMultiset


@pytest.fixture
def multiset() -> SortedMultiset:
    return SortedMultiset()


@pytest.fixture
def multiset_with_values() -> SortedMultiset:
    return SortedMultiset(
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5,
            8, 9, 7, 9, 3, 2, 3, 8, 4, 6]
    )


class TestSortedSet:

    def test_add(self, multiset: SortedMultiset) -> None:
        assert multiset.a == []
        assert len(multiset.a) == 0

        expected = [[[1]], [[1, 2]], [[1, 2, 3]]]

        for i in range(1, 3 + 1):
            multiset.add(i)  # type: ignore
            assert multiset.a == expected[i - 1]  # 0-indexed.

            assert len(multiset.a) == 1
            assert len(multiset.a[0]) == i

        multiset.add(2)
        assert multiset.a == [[1, 2, 2, 3]]  # 0-indexed.

    def test_discard(self, multiset: SortedMultiset) -> None:
        assert multiset.a == []

        expected = [[[1]], [[1, 2]], [[1, 2, 3]]]

        for i in range(1, 3 + 1):
            multiset.add(i)  # type: ignore
            assert multiset.a == expected[i - 1]  # 0-indexed.

        multiset.add(2)  # type: ignore
        assert multiset.a == [[1, 2, 2, 3]]
        assert len(multiset.a[0]) == 4

        multiset.discard(2)  # type: ignore
        assert multiset.a == [[1, 2, 3]]
        assert len(multiset.a[0]) == 3

        multiset.discard(2)  # type: ignore
        assert multiset.a == [[1, 3]]
        assert len(multiset.a[0]) == 2

        multiset.discard(4)  # type: ignore
        assert multiset.a == [[1, 3]]
        assert len(multiset.a[0]) == 2

        multiset.discard(0)  # type: ignore
        assert multiset.a == [[1, 3]]
        assert len(multiset.a[0]) == 2

        multiset.discard(1)  # type: ignore
        assert multiset.a == [[3]]
        assert len(multiset.a[0]) == 1

        multiset.discard(3)  # type: ignore
        assert multiset.a == []
        assert len(multiset.a) == 0

    @pytest.mark.parametrize(('base', 'expected'), [
        (1, None),
        (2, 1),
        (3, 2),
        (9, 8),
        (10, 9),
        (11, 9),
    ])
    def test_lt(
            self,
            multiset_with_values: SortedMultiset,
            base: int,
            expected: int
            ) -> None:
        actual = multiset_with_values.lt(base)  # type: ignore
        assert actual == expected

    @pytest.mark.parametrize(('base', 'expected'), [
        (0, None),
        (1, 1),
        (2, 2),
        (9, 9),
        (10, 9),
        (11, 9),
    ])
    def test_le(
            self,
            multiset_with_values: SortedMultiset,
            base: int,
            expected: int
            ) -> None:
        actual = multiset_with_values.le(base)  # type: ignore
        assert actual == expected

    @pytest.mark.parametrize(('base', 'expected'), [
        (0, 1),
        (1, 2),
        (2, 3),
        (8, 9),
        (9, None),
        (10, None),
    ])
    def test_gt(
            self,
            multiset_with_values: SortedMultiset,
            base: int,
            expected: int
            ) -> None:
        actual = multiset_with_values.gt(base)  # type: ignore
        assert actual == expected

    @pytest.mark.parametrize(('base', 'expected'), [
        (0, 1),
        (1, 1),
        (2, 2),
        (8, 8),
        (9, 9),
        (10, None),
    ])
    def test_ge(
            self,
            multiset_with_values: SortedMultiset,
            base: int,
            expected: int
            ) -> None:
        actual = multiset_with_values.ge(base)  # type: ignore
        assert actual == expected

    def test_exists_element(
            self,
            multiset_with_values: SortedMultiset
            ) -> None:
        for x in range(1, 10):
            assert x in multiset_with_values  # type: ignore

    @pytest.mark.parametrize('x', [
        -1,
        0,
        10,
        11,
        100,
    ])
    def test_not_exists_element(
            self,
            multiset_with_values: SortedMultiset,
            x: int
            ) -> None:
        assert x not in multiset_with_values  # type: ignore

    @pytest.mark.parametrize(('x', 'expected'), [
        (0, 1),
        (1, 1),
        (2, 2),
        (17, 8),
        (18, 9),
        (19, 9),
        (20, 9),
    ])
    def test_xth_element_from_min_value(
            self,
            multiset_with_values: SortedMultiset,
            x: int,
            expected: int
            ) -> None:
        assert multiset_with_values[x] == expected  # 0-indexed.

    @pytest.mark.parametrize(('x', 'expected'), [
        (0, 9),
        (1, 9),
        (2, 9),
        (3, 8),
        (18, 2),
        (19, 1),
        (20, 1),
    ])
    def test_xth_element_from_max_value(
            self,
            multiset_with_values: SortedMultiset,
            x: int,
            expected: int
            ) -> None:
        assert multiset_with_values[~x] == expected  # 0-indexed.

    @pytest.mark.parametrize(('base', 'expected'), [
        (0, 0),
        (1, 0),
        (2, 2),
        (3, 4),
        (9, 18),
        (10, 21),
        (100, 21),
    ])
    def test_index(
            self,
            multiset_with_values: SortedMultiset,
            base: int,
            expected: int
            ) -> None:
        actual = multiset_with_values.index(base)  # type: ignore
        assert actual == expected

    @pytest.mark.parametrize(('base', 'expected'), [
        (0, 0),
        (1, 2),
        (2, 4),
        (8, 18),
        (9, 21),
        (10, 21),
        (100, 21),
    ])
    def test_index_right(
            self,
            multiset_with_values: SortedMultiset,
            base: int,
            expected: int
            ) -> None:
        actual = multiset_with_values.index_right(base)  # type: ignore
        assert actual == expected

    @pytest.mark.parametrize(('base', 'expected'), [
        (0, 0),
        (1, 2),
        (2, 2),
        (8, 2),
        (9, 3),
        (10, 0),
        (100, 0),
    ])
    def test_count(
            self,
            multiset_with_values: SortedMultiset,
            base: int,
            expected: int
            ) -> None:
        actual = multiset_with_values.count(base)  # type: ignore
        assert actual == expected
