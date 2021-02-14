# -*- coding: utf-8 -*-

import pytest
from snippets.graph.rooted_tree import calc_depth, run_imos


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

    @pytest.mark.parametrize(
        ("graph", "depth", "imos", "expected"),
        [(
            [
                [1],
                [0, 2, 3],
                [1],
                [1, 4],
                [3]
            ],
            [0, 1, 2, 2, 3],
            [11, 99, 1000, 0, -10],
            [11, 110, 1110, 110, 100],
         ),
         (

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
            [72, -64, 5, 18, 32, 0, -8],
            [72, 8, 13, 26, 58, 72, 5],
         ),
         (
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
            [1657, 0, 452, -406, -183, 0, 1545, 0, -862, 0, 856],
            [1657, 1657, 2109, 1703, 1474, 1657, 3202, 1474, 1247, 2109, 2559],
         ),
        ]
    )
    def test_run_imos(self, graph, depth, imos, expected):
        actual = run_imos(graph, depth, imos)
        assert actual == expected
