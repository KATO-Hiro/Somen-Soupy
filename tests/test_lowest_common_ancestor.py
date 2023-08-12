from typing import List

import pytest

from snippets.graph.lowest_common_ancestor import LowestCommonAncestor


@pytest.fixture
def graph() -> List[List[int]]:
    n = 11

    inputs: List[List[int]] = [
        [1, 2],
        [2, 3],
        [3, 5],
        [3, 6],
        [2, 4],
        [4, 7],
        [1, 8],
        [8, 9],
        [8, 10],
        [9, 11],
    ]

    graph = [[] for _ in range(n)]

    for i in range(n - 1):
        ai, bi = inputs[i]
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    return graph


class TestLowestCommonAncestor:
    @pytest.mark.parametrize(
        ("ui", "vi", "expected"),
        [
            (0, 0, 0),
            (0, 1, 0),
            (2, 3, 1),
            (5, 6, 1),
            (8, 9, 7),
            (10, 4, 0),
            (10, 10, 10),
        ],
    )
    def test_lca(self, graph: List[List[int]], ui: int, vi: int, expected: int) -> None:
        root = 0
        tree = LowestCommonAncestor(graph=graph, root=root)
        actual = tree.lca(ui, vi)

        assert actual == expected

    @pytest.mark.parametrize(
        ("ui", "vi", "expected"),
        [
            (0, 0, 0),
            (0, 1, 1),
            (2, 3, 2),
            (5, 6, 4),
            (8, 9, 2),
            (10, 4, 6),
            (10, 10, 0),
        ],
    )
    def test_calc_dist(
        self, graph: List[List[int]], ui: int, vi: int, expected: int
    ) -> None:
        root = 0
        tree = LowestCommonAncestor(graph=graph, root=root)
        actual = tree.calc_dist(ui, vi)

        assert actual == expected

    @pytest.mark.parametrize(
        ("ui", "vi", "ai", "expected"),
        [
            (0, 1, 0, True),
            (0, 1, 1, True),
            (0, 1, 2, False),
            (0, 1, 3, False),
            (0, 1, 7, False),
            (5, 6, 0, False),
            (5, 6, 4, False),
            (5, 6, 1, True),
            (5, 6, 2, True),
            (5, 6, 3, True),
            (5, 6, 5, True),
            (5, 6, 6, True),
            (10, 4, 3, False),
            (10, 4, 5, False),
            (10, 4, 6, False),
            (10, 4, 9, False),
            (10, 4, 2, True),
            (10, 4, 8, True),
        ],
    )
    def test_is_on_path(
        self, graph: List[List[int]], ui: int, vi: int, ai: int, expected: bool
    ) -> None:
        root = 0
        tree = LowestCommonAncestor(graph=graph, root=root)
        actual = tree.is_on_path(ui, vi, ai)

        assert actual == expected

    @pytest.mark.parametrize(
        ("ui", "vi"),
        [
            (-2, 8),
            (-1, 8),
            (0, 11),
            (0, 12),
            (-2, 11),
            (-2, 12),
            (-1, 11),
            (-1, 12),
        ],
    )
    def test_lca_failed_if_invalid_input_is_given(
        self, graph: List[List[int]], ui: int, vi: int
    ) -> None:
        root = 0
        tree = LowestCommonAncestor(graph=graph, root=root)

        with pytest.raises(AssertionError):
            tree.lca(ui, vi)

    @pytest.mark.parametrize(
        ("ui", "vi"),
        [
            (-2, 8),
            (-1, 8),
            (0, 11),
            (0, 12),
            (-2, 11),
            (-2, 12),
            (-1, 11),
            (-1, 12),
        ],
    )
    def test_calc_dist_failed_if_invalid_input_is_given(
        self, graph: List[List[int]], ui: int, vi: int
    ) -> None:
        root = 0
        tree = LowestCommonAncestor(graph=graph, root=root)

        with pytest.raises(AssertionError):
            tree.calc_dist(ui, vi)

    @pytest.mark.parametrize(
        ("ui", "vi", "ai"),
        [
            (-2, 8, 0),
            (-1, 8, 0),
            (0, 11, 6),
            (0, 12, 4),
            (0, 10, -1),
            (0, 10, -2),
            (-2, 11, -1),
            (-2, 12, -1),
            (-1, 11, -1),
            (-1, 12, -1),
        ],
    )
    def test_is_on_path_failed_if_invalid_input_is_given(
        self, graph: List[List[int]], ui: int, vi: int, ai: int
    ) -> None:
        root = 0
        tree = LowestCommonAncestor(graph=graph, root=root)

        with pytest.raises(AssertionError):
            tree.is_on_path(ui, vi, ai)
