# -*- coding: utf-8 -*-


from typing import List, Tuple

import pytest

from snippets.graph.bipartite import is_bipartite


class TestIsBipartite:
    @pytest.mark.parametrize(
        ("number", "graph", "expected"),
        [
            (5, [[2], [2, 3, 4], [1], [1], [1]], (True, 2, 3)),
            (3, [[1, 2], [0, 2], [0, 1]], (False, 0, 0)),
        ],
    )
    def test_is_bipartite(
        self, number: int, graph: List[List[int]], expected: Tuple[bool, int, int]
    ) -> None:
        colors = [0] * number
        actual = is_bipartite(0, graph, colors)

        assert actual == expected

    def test_is_bipartite_when_multiple_connected_components_are_given(self) -> None:
        number = 5
        no_color = 0
        colors = [no_color] * number
        graph = [[1], [0], [3], [2, 4], [3]]
        expected = [(True, 1, 1), (True, 2, 1)]
        used_count = 0

        for i in range(number):
            if colors[i] != no_color:
                continue

            actual = is_bipartite(i, graph, colors)
            assert actual == expected[used_count]

            used_count += 1
