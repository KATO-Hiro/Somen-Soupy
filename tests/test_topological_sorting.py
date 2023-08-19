# -*- coding: utf-8 -*-

from typing import List, Tuple

import pytest

from snippets.graph.topological_sorting import TopologicalSorting


class TestTopologicalSorting:
    @pytest.mark.parametrize(
        ("n", "m", "graph", "expected"),
        [
            (3, 2, [[3, 1], [2, 3]], (True, [1, 2, 0])),
            (4, 3, [[1, 2], [2, 3], [3, 4]], (True, [0, 1, 2, 3])),
            (3, 2, [[3, 1], [3, 2]], (False, [])),
            (3, 0, [], (False, [])),
        ],
    )
    def test_topological_sorting(
        self, n: int, m: int, graph: List[List[int]], expected: Tuple[bool, List[int]]
    ) -> None:
        ts = TopologicalSorting(n)

        for i in range(m):
            # vertex ai -> bi.
            ai, bi = graph[i]
            ai -= 1
            bi -= 1

            ts.add_edge(frm=ai, to=bi)

        is_DAG, orders = ts.sort()
        expected_is_DAG, expected_orders = expected

        assert is_DAG == expected_is_DAG
        assert orders == expected_orders

    @pytest.mark.parametrize(
        ("n", "m", "graph", "expected"),
        [
            (
                6,
                5,
                [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],
                (True, [1, 2, 3, 4, 5, 6]),
            ),
            (8, 4, [[1, 5], [2, 6], [3, 7], [4, 8]], (True, [1, 5])),
            (
                6,
                6,
                [[1, 2], [1, 3], [1, 4], [2, 3], [2, 5], [4, 5]],
                (True, [1, 2, 4, 3, 5]),
            ),
        ],
    )
    def test_topological_sorting_only_reachable_vertices_from(
        self, n: int, m: int, graph: List[List[int]], expected: Tuple[bool, List[int]]
    ) -> None:
        ts = TopologicalSorting(n)

        for i in range(m):
            # vertex ai -> bi.
            ai, bi = graph[i]
            ai -= 1
            bi -= 1

            ts.add_edge(frm=ai, to=bi)

        is_DAG, orders = ts.sort_only_reachable_vertices_from(start_id=0)
        expected_is_DAG, expected_orders = expected

        assert is_DAG == expected_is_DAG
        assert orders == expected_orders
