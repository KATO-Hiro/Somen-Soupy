# -*- coding: utf-8 -*-

from typing import List

import pytest

from snippets.graph.unionfind import UnionFind, UnionFind2D


class TestUnionFind:
    def test_find_root(self):
        number = 5
        uf = UnionFind(number)

        actual = uf.find_root(0)
        expected = 0
        assert actual == expected

        # Merge element 0, 1, 2.
        uf.merge_if_needs(0, 1)
        uf.merge_if_needs(0, 2)
        actual = uf.find_root(2)
        expected = 0
        assert actual == expected

    def test_get_group_size(self):
        number = 5
        uf = UnionFind(number)

        actual = uf.get_group_size(0)
        expected = 1
        assert actual == expected

        # Merge element 0 and 1.
        uf.merge_if_needs(0, 1)
        actual = uf.get_group_size(0)
        expected = 2
        assert actual == expected

    def test_is_same_group(self):
        number = 5
        uf = UnionFind(number)

        actual = uf.is_same_group(0, 1)
        expected = False
        assert actual == expected

        actual = uf.is_same_group(0, 2)
        expected = False
        assert actual == expected

        # Merge element 0, 1.
        uf.merge_if_needs(0, 1)
        actual = uf.is_same_group(0, 1)
        expected = True
        assert actual == expected

        # Element 0 and 2 are not the same group.
        actual = uf.is_same_group(0, 2)
        expected = False
        assert actual == expected

    def test_get_roots(self):
        number = 5
        uf = UnionFind(number)

        assert uf.get_roots() == [i for i in range(number)]

        uf.merge_if_needs(0, 1)
        assert uf.get_roots() == [0, 2, 3, 4]

    def test_get_groups(self) -> None:
        number = 10
        uf = UnionFind(number)

        uf.merge_if_needs(0, 1)
        uf.merge_if_needs(3, 8)
        uf.merge_if_needs(8, 5)

        assert uf.get_groups() == [[0, 1], [2], [3, 5, 8], [4], [6], [7], [9]]

    def test_edge_count(self):
        number = 5
        uf = UnionFind(number)

        assert uf.get_edge_count(0) == 0

        uf.merge_if_needs(0, 1)
        assert uf.get_edge_count(0) == 1

    def test_get_group_count(self):
        number = 5
        uf = UnionFind(number)

        assert uf.get_group_count() == 5

        for i in range(1, number):
            uf.merge_if_needs(0, i)
            assert uf.get_group_count() == 5 - i


@pytest.fixture
def grid() -> List[List[str]]:
    grid_sample = [
        [".", ".", ".", "#", ".", ".", "#", ".", "."],
        [".", "#", ".", ".", ".", "#", ".", ".", "#"],
        [".", ".", "#", "#", "#", "#", "#", ".", "#"],
        ["#", ".", ".", ".", "#", ".", ".", "#", "."],
        ["#", ".", ".", ".", "#", ".", ".", ".", "."],
        [".", ".", ".", ".", "#", ".", "#", ".", "#"],
    ]

    return grid_sample


@pytest.fixture
def union_find_2d(grid: List[List[str]]) -> UnionFind2D:
    height, width = 6, 9
    uf_2d = UnionFind2D(height=height, width=width)

    for row in range(height):
        for column in range(width):
            if grid[row][column] == "#":
                continue

            if row + 1 < height and grid[row + 1][column] == ".":
                uf_2d.merge_if_needs(column, row, column, row + 1)
            if column + 1 < width and grid[row][column + 1] == ".":
                uf_2d.merge_if_needs(column, row, column + 1, row)

    return uf_2d


class TestUnionFind2D:
    @pytest.mark.parametrize(
        ("x", "y", "expected"),
        [(0, 0, 0), (0, 1, 0), (7, 0, 7), (8, 0, 7), (5, 3, 32), (6, 3, 32)],
    )
    def test_find_root(
        self, union_find_2d: UnionFind2D, x: int, y: int, expected: int
    ) -> None:
        actual = union_find_2d.find_root(x, y)
        assert actual == expected

    @pytest.mark.parametrize(
        ("x", "y", "expected"),
        [
            (0, 0, 21),
            (8, 0, 5),
            (6, 4, 9),
        ],
    )
    def test_get_group_size(
        self, union_find_2d: UnionFind2D, x: int, y: int, expected: int
    ) -> None:
        actual = union_find_2d.get_group_size(x, y)
        assert actual == expected

    @pytest.mark.parametrize(
        ("x1", "y1", "x2", "y2", "expected"),
        [
            (0, 0, 0, 0, True),
            (0, 0, 3, 5, True),
            (5, 5, 8, 3, True),
            (0, 0, 8, 0, False),
            (0, 0, 8, 3, False),
            (2, 2, 2, 3, False),
        ],
    )
    def test_is_same_group(
        self,
        union_find_2d: UnionFind2D,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        expected: bool,
    ) -> None:
        actual = union_find_2d.is_same_group(x1, y1, x2, y2)
        assert actual == expected

    def test_get_group_count(
        self, grid: List[List[str]], union_find_2d: UnionFind2D
    ) -> None:
        actual = union_find_2d.get_group_count()
        expected = 22

        assert actual == expected

    def test_get_roots(self, union_find_2d: UnionFind2D) -> None:
        actual = union_find_2d.get_roots()
        expected = [
            0,
            3,
            6,
            7,
            10,
            14,
            17,
            20,
            21,
            22,
            23,
            24,
            26,
            27,
            31,
            32,
            34,
            36,
            40,
            49,
            51,
            53,
        ]

        assert actual == expected

    def test_get_groups(self, union_find_2d: UnionFind2D) -> None:
        actual = union_find_2d.get_groups()
        expected = [
            [
                0,
                1,
                2,
                4,
                5,
                9,
                11,
                12,
                13,
                18,
                19,
                28,
                29,
                30,
                37,
                38,
                39,
                45,
                46,
                47,
                48,
            ],
            [3],
            [6],
            [7, 8, 15, 16, 25],
            [10],
            [14],
            [17],
            [20],
            [21],
            [22],
            [23],
            [24],
            [26],
            [27],
            [31],
            [32, 33, 35, 41, 42, 43, 44, 50, 52],
            [34],
            [36],
            [40],
            [49],
            [51],
            [53],
        ]

        assert actual == expected

    @pytest.mark.parametrize(
        ("number", "expected"),
        [
            (0, (0, 0)),
            (1, (0, 1)),
            (8, (0, 8)),
            (9, (1, 0)),
            (10, (1, 1)),
            (17, (1, 8)),
            (45, (5, 0)),
            (53, (5, 8)),
        ],
    )
    def test_to_yx(
        self, union_find_2d: UnionFind2D, number: int, expected: tuple[int, int]
    ) -> None:
        actual = union_find_2d._to_yx(number)

        assert actual == expected

    @pytest.mark.parametrize(
        ("x", "y"),
        [
            (-2, 0),
            (-1, 0),
            (9, 0),
            (10, 0),
            (0, -2),
            (0, -1),
            (0, 6),
            (0, 7),
            (-2, 6),
            (-2, 7),
            (-1, 6),
            (-1, 7),
            (9, -2),
            (10, -2),
            (9, -1),
            (10, -1),
        ],
    )
    def test_find_root_failed_if_invalid_input_is_given(
        self, union_find_2d: UnionFind2D, x: int, y: int
    ) -> None:
        with pytest.raises(AssertionError):
            union_find_2d.find_root(x, y)

    @pytest.mark.parametrize(
        ("x", "y"),
        [
            (-2, 0),
            (-1, 0),
            (9, 0),
            (10, 0),
            (0, -2),
            (0, -1),
            (0, 6),
            (0, 7),
            (-2, 6),
            (-2, 7),
            (-1, 6),
            (-1, 7),
            (9, -2),
            (10, -2),
            (9, -1),
            (10, -1),
        ],
    )
    def test_group_size_failed_if_invalid_input_is_given(
        self, union_find_2d: UnionFind2D, x: int, y: int
    ) -> None:
        with pytest.raises(AssertionError):
            union_find_2d.get_group_size(x, y)

    @pytest.mark.parametrize(
        ("x1", "y1", "x2", "y2"),
        [
            (-2, 0, 0, 0),
            (-1, 0, 0, 0),
            (0, 0, -1, 0),
            (0, 0, 9, 0),
            (9, 0, 0, 0),
            (10, 0, 0, 0),
            (0, -2, 0, 0),
            (0, -1, 0, 0),
            (0, 0, 0, -1),
            (0, 6, 0, 0),
            (0, 7, 0, 0),
            (0, 0, 0, 6),
        ],
    )
    def test_is_same_group_failed_if_invalid_input_is_given(
        self, union_find_2d: UnionFind2D, x1: int, y1: int, x2: int, y2: int
    ) -> None:
        with pytest.raises(AssertionError):
            union_find_2d.is_same_group(x1, y1, x2, y2)

    @pytest.mark.parametrize(
        ("x1", "y1", "x2", "y2"),
        [
            (-2, 0, 0, 0),
            (-1, 0, 0, 0),
            (0, 0, -1, 0),
            (0, 0, 9, 0),
            (9, 0, 0, 0),
            (10, 0, 0, 0),
            (0, -2, 0, 0),
            (0, -1, 0, 0),
            (0, 0, 0, -1),
            (0, 6, 0, 0),
            (0, 7, 0, 0),
            (0, 0, 0, 6),
        ],
    )
    def test_merge_if_needs_failed_if_invalid_input_is_given(
        self, union_find_2d: UnionFind2D, x1: int, y1: int, x2: int, y2: int
    ) -> None:
        with pytest.raises(AssertionError):
            union_find_2d.merge_if_needs(x1, y1, x2, y2)
