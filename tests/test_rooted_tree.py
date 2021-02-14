# -*- coding: utf-8 -*-

import pytest
from snippets.graph.rooted_tree import calc_depth


class TestRootedTree:
    @pytest.mark.parametrize(
        ("vertex_count", "graph", "expected"),
        [
            (
                5,
                [
                    [1],
                    [0, 2, 3],
                    [1],
                    [1, 4],
                    [3]
                ],
                [0, 1, 2, 2, 3]
            ),
            (
                7,
                [
                    [1, 5],
                    [0, 2, 3],
                    [1, 6],
                    [1, 4],
                    [3],
                    [0],
                    [2]
                ],
                [0, 1, 2, 2, 3, 1, 3],
            ),
            (
                11,
                [
                    [1, 2, 5, 6],
                    [0, 4],
                    [0, 3, 8, 9],
                    [2, 10],
                    [1, 7],
                    [0],
                    [0],
                    [4],
                    [2],
                    [2],
                    [3],
                ],
                [0, 1, 1, 2, 2, 1, 1, 3, 2, 2, 3],
            ),
        ],
    )
    def test_calc_depth(self, vertex_count, graph, expected):
        actual = calc_depth(vertex_count, graph)
        assert actual == expected
