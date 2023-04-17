# -*- coding: utf-8 -*-


from typing import List
import pytest

from snippets.graph.bipartite import is_bipartite


class TestMatrixRotation:
    @pytest.mark.parametrize(
        ("number", "graph", "expected"),
        [
            (5, [[2], [2, 3, 4], [1], [1], [1]], True),
            (3, [[1, 2], [0, 2], [0, 1]], False),
        ],
    )
    def test_is_bipartite(self, number: int, graph: List[List[int]], expected: bool):
        colors = [0] * number
        actual = is_bipartite(0, graph, colors)

        assert actual == expected