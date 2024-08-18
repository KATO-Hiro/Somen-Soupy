import pytest

from snippets.technique.finder import NOT_FOUND, Finder


@pytest.fixture
def array() -> list[int]:
    return [3, 6, 7, 2, 5, 5, 1, 10, 8, 5]


class TestFinder:
    def test_auto_init_without_array(self) -> None:
        finder = Finder()

        assert finder.get_size() == 0
        assert finder.is_empty()

    def test_auto_init(self, array: list[int]) -> None:
        finder = Finder(array)

        assert finder.get_size() == 10
        assert not finder.is_empty()

    def test_auto_init_with_offset(self, array: list[int]) -> None:
        finder = Finder(array, offset=-10)

        assert finder.get_size() == 10
        assert len(finder.indexes) == 21

    def test_manual_init(self, array: list[int]) -> None:
        finder = Finder()
        finder.init(array)

        assert finder.get_size() == 10
        assert not finder.is_empty()

    def test_manual_init_with_offset(self, array: list[int]) -> None:
        finder = Finder()
        finder.init(array, offset=-10)

        assert finder.get_size() == 10
        assert len(finder.indexes) == 21

    def test_append_an_element(self, array: list[int]) -> None:
        finder = Finder(array)
        finder.append(5)

        assert finder.get_size() == 11
        assert finder.find_indexes(5) == [4, 5, 9, 10]

    def test_append_multiple_elements(self, array: list[int]) -> None:
        finder = Finder(array)
        finder.append_list([12, 13, 14])

        assert finder.get_size() == 13
        assert finder.find_indexes(12) == [10]
        assert finder.find_indexes(13) == [11]
        assert finder.find_indexes(14) == [12]

    def test_pop(self, array: list[int]) -> None:
        finder = Finder(array)
        size = finder.get_size()

        assert size == 10

        for ai in array[::-1]:
            value = finder.pop()
            size -= 1
            assert value == ai
            assert finder.get_size() == size

        assert finder.is_empty()

    def test_clear(self, array: list[int]) -> None:
        finder = Finder(array)
        finder.clear()

        assert finder.is_empty()

    def test_find_indexes(self, array: list[int]) -> None:
        finder = Finder(array)

        assert finder.find_indexes(3) == [0]
        assert finder.find_indexes(2) == [3]
        assert finder.find_indexes(5) == [4, 5, 9]
        assert finder.find_indexes(8) == [8]

    @pytest.mark.parametrize(
        ("value", "right", "expected"),
        [
            (3, 0, 0),
            (5, 0, 4),
            (5, 1, 5),
            (5, 2, 9),
            (5, 3, -1),
            (11, 0, -1),
        ],
    )
    def test_find_index(
        self, array: list[int], value: int, right: int, expected: int
    ) -> None:
        finder = Finder(array)
        assert finder.find_index(value, right) == expected

    @pytest.mark.parametrize(
        ("index", "value", "expected"),
        [
            (0, 7, 2),
            (1, 7, 2),
            (2, 7, -1),
            (0, 5, 4),
            (3, 5, 4),
            (4, 5, 5),
            (5, 5, 9),
            (9, 5, -1),
        ],
    )
    def test_find_next_index(
        self, array: list[int], index: int, value: int, expected: int
    ) -> None:
        finder = Finder(array)

        assert finder.find_next_index(index, value) == expected

    @pytest.mark.parametrize(
        ("index", "value", "expected"),
        [
            (0, 7, -1),
            (2, 7, -1),
            (3, 7, 2),
            (0, 5, -1),
            (3, 5, -1),
            (4, 5, -1),
            (5, 5, 4),
            (9, 5, 5),
        ],
    )
    def test_find_prev_index(
        self, array: list[int], index: int, value: int, expected: int
    ) -> None:
        finder = Finder(array)
        assert finder.find_prev_index(index, value) == expected

    @pytest.mark.parametrize(
        ("index", "value", "expected"),
        [
            (0, 7, 2),
            (1, 7, 2),
            (2, 7, 2),
            (3, 7, -1),
            (0, 5, 4),
            (3, 5, 4),
            (4, 5, 4),
            (5, 5, 5),
            (6, 5, 9),
            (9, 5, 9),
        ],
    )
    def test_find_ceil_index(
        self, array: list[int], index: int, value: int, expected: int
    ) -> None:
        finder = Finder(array)
        assert finder.find_ceil_index(index, value) == expected

    @pytest.mark.parametrize(
        ("index", "value", "expected"),
        [
            (0, 7, -1),
            (1, 7, -1),
            (2, 7, 2),
            (3, 7, 2),
            (0, 5, -1),
            (3, 5, -1),
            (4, 5, 4),
            (5, 5, 5),
            (8, 5, 5),
            (9, 5, 9),
        ],
    )
    def test_find_floor_index(
        self, array: list[int], index: int, value: int, expected: int
    ) -> None:
        finder = Finder(array)
        assert finder.find_floor_index(index, value) == expected

    @pytest.mark.parametrize(
        ("index", "value", "expected"),
        [
            (0, 7, 2),
            (1, 7, 2),
            (2, 7, 2),
            (0, 5, 4),
            (3, 5, 4),
            (4, 5, 5),
            (5, 5, 9),
            (9, 5, 4),
            (11, 0, -1),
        ],
    )
    def test_find_cycle_next_index(
        self, array: list[int], index: int, value: int, expected: int
    ) -> None:
        finder = Finder(array)
        assert finder.find_cycle_next_index(index, value) == expected

    @pytest.mark.parametrize(
        ("index", "value", "expected"),
        [
            (0, 7, 2),
            (2, 7, 2),
            (3, 7, 2),
            (0, 5, 9),
            (3, 5, 9),
            (4, 5, 9),
            (5, 5, 4),
            (9, 5, 5),
            (11, 9, -1),
        ],
    )
    def test_find_cycle_prev_index(
        self, array: list[int], index: int, value: int, expected: int
    ) -> None:
        finder = Finder(array)
        assert finder.find_cycle_prev_index(index, value) == expected

    @pytest.mark.parametrize(
        ("index", "value", "expected"),
        [
            (0, 7, 2),
            (1, 7, 2),
            (2, 7, 2),
            (0, 5, 4),
            (3, 5, 4),
            (4, 5, 4),
            (5, 5, 5),
            (6, 5, 9),
            (8, 5, 9),
            (9, 5, 9),
            (11, 0, -1),
        ],
    )
    def test_find_cycle_ceil_index(
        self, array: list[int], index: int, value: int, expected: int
    ) -> None:
        finder = Finder(array)
        assert finder.find_cycle_ceil_index(index, value) == expected

    @pytest.mark.parametrize(
        ("index", "value", "expected"),
        [
            (0, 7, 2),
            (2, 7, 2),
            (3, 7, 2),
            (0, 5, 9),
            (3, 5, 9),
            (4, 5, 4),
            (5, 5, 5),
            (8, 5, 5),
            (9, 5, 9),
            (11, 9, -1),
        ],
    )
    def test_find_cycle_floor_index(
        self, array: list[int], index: int, value: int, expected: int
    ) -> None:
        finder = Finder(array)
        assert finder.find_cycle_floor_index(index, value) == expected

    @pytest.mark.parametrize(
        ("value", "left", "right", "expected"),
        [
            (7, 0, 1, 0),
            (7, 0, 2, 1),
            (7, 0, 3, 1),
            (7, 0, 9, 1),
            (5, 0, 9, 3),
            (5, 0, 3, 0),
            (5, 0, 4, 1),
            (5, 0, 5, 2),
            (5, 0, 6, 2),
            (5, 0, 8, 2),
            (5, 0, 9, 3),
            (5, 3, 3, 0),
            (5, 4, 4, 1),
            (5, 4, 5, 2),
            (5, 4, 6, 2),
            (5, 4, 8, 2),
            (5, 4, 9, 3),
            (5, 5, 5, 1),
            (5, 5, 6, 1),
            (5, 5, 8, 1),
            (5, 5, 9, 2),
            (5, 9, 9, 1),
            (11, 0, 9, 0),
        ],
    )
    def test_count_values_in_ranges(
        self, array: list[int], value: int, left: int, right: int, expected: int
    ) -> None:
        finder = Finder(array)
        assert finder.count_values_in_ranges(value, left, right) == expected


class TestFinderForEdgeCases:
    @pytest.mark.parametrize(
        ("value", "expected"),
        [
            (10**12, [NOT_FOUND]),
            (-2, [NOT_FOUND]),
            (-1, [NOT_FOUND]),
            (11, [NOT_FOUND]),
            (12, [NOT_FOUND]),
            (10**12, [NOT_FOUND]),
        ],
    )
    def test_find_indexes_when_out_of_ranges_are_given(
        self, array: list[int], value: int, expected: int
    ) -> None:
        finder = Finder(array)
        assert finder.find_indexes(value) == expected

    @pytest.mark.parametrize(
        ("value", "right", "expected"),
        [
            (3, 1, NOT_FOUND),
            (3, 2, NOT_FOUND),
            (5, 3, NOT_FOUND),
            (5, 4, NOT_FOUND),
            (5, 10**12, NOT_FOUND),
            (11, 0, NOT_FOUND),
            (11, 1, NOT_FOUND),
        ],
    )
    def test_find_index_when_out_of_ranges_are_given(
        self, array: list[int], value: int, right: int, expected: int
    ) -> None:
        finder = Finder(array)
        assert finder.find_index(value, right) == expected

    @pytest.mark.parametrize(
        ("index", "value", "expected"),
        [
            (0, -1, NOT_FOUND),
            (9, -1, NOT_FOUND),
            (0, 11, NOT_FOUND),
            (9, 11, NOT_FOUND),
            (0, 12, NOT_FOUND),
            (9, 12, NOT_FOUND),
            (0, 10**12 + 1, NOT_FOUND),
            (9, 10**12 + 1, NOT_FOUND),
        ],
    )
    def test_find_next_index_when_out_of_offsets_are_given(
        self, array: list[int], index: int, value: int, expected: int
    ) -> None:
        finder = Finder(array)
        assert finder.find_next_index(index, value) == expected

    @pytest.mark.parametrize(
        ("index", "value", "expected"),
        [
            (10, 7, NOT_FOUND),
            (10, 5, NOT_FOUND),
            (11, 5, NOT_FOUND),
            (10**12 + 1, 5, NOT_FOUND),
            (10**18, 5, NOT_FOUND),
        ],
    )
    def test_find_next_index_when_out_of_ranges_are_given(
        self, array: list[int], index: int, value: int, expected: int
    ) -> None:
        finder = Finder(array)
        assert finder.find_next_index(index, value) == expected

    @pytest.mark.parametrize(
        ("index", "value", "expected"),
        [
            (0, -1, NOT_FOUND),
            (9, -1, NOT_FOUND),
            (0, 11, NOT_FOUND),
            (9, 11, NOT_FOUND),
            (0, 12, NOT_FOUND),
            (9, 12, NOT_FOUND),
            (0, 10**12 + 1, NOT_FOUND),
            (9, 10**12 + 1, NOT_FOUND),
        ],
    )
    def test_find_prev_index_when_out_of_offsets_are_given(
        self, array: list[int], index: int, value: int, expected: int
    ) -> None:
        finder = Finder(array)
        assert finder.find_prev_index(index, value) == expected

    @pytest.mark.parametrize(
        ("index", "value", "expected"),
        [
            (-2, 7, NOT_FOUND),
            (-1, 7, NOT_FOUND),
            (0, 7, NOT_FOUND),
            (-2, 5, NOT_FOUND),
            (-1, 5, NOT_FOUND),
            (0, 5, NOT_FOUND),
        ],
    )
    def test_find_prev_index_when_out_of_ranges_are_given(
        self, array: list[int], index: int, value: int, expected: int
    ) -> None:
        finder = Finder(array)
        assert finder.find_prev_index(index, value) == expected

    @pytest.mark.parametrize(
        ("index", "value", "expected"),
        [
            (0, -1, NOT_FOUND),
            (9, -1, NOT_FOUND),
            (0, 11, NOT_FOUND),
            (9, 11, NOT_FOUND),
            (0, 12, NOT_FOUND),
            (9, 12, NOT_FOUND),
            (0, 10**12 + 1, NOT_FOUND),
            (9, 10**12 + 1, NOT_FOUND),
        ],
    )
    def test_find_cycle_next_index_when_out_of_offsets_are_given(
        self, array: list[int], index: int, value: int, expected: int
    ) -> None:
        finder = Finder(array)
        assert finder.find_cycle_next_index(index, value) == expected

    @pytest.mark.parametrize(
        ("index", "value", "expected"),
        [
            (0, -1, NOT_FOUND),
            (9, -1, NOT_FOUND),
            (0, 11, NOT_FOUND),
            (9, 11, NOT_FOUND),
            (0, 12, NOT_FOUND),
            (9, 12, NOT_FOUND),
            (0, 10**12 + 1, NOT_FOUND),
            (9, 10**12 + 1, NOT_FOUND),
        ],
    )
    def test_find_cycle_prev_index_when_out_of_offsets_are_given(
        self, array: list[int], index: int, value: int, expected: int
    ) -> None:
        finder = Finder(array)
        assert finder.find_cycle_prev_index(index, value) == expected
