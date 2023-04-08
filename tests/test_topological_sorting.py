# -*- coding: utf-8 -*-

from typing import List, Tuple
import pytest

from snippets.graph.topological_sorting import TopologicalSorting


class TestTopologicalSorting:

    @pytest.mark.parametrize(('n', 'm', 'graph', 'expected'), [
        (3, 2, [[3, 1], [2, 3]], (True, [1, 2, 0])),
        (4, 3, [[1, 2], [2, 3], [3, 4]], (True, [0, 1, 2, 3])),
        (3, 2, [[3, 1], [3, 2]], (False, [])),
        (3, 0, [], (False, [])),
    ])
    def test_topological_sorting(self, n: int, m: int, graph: List[List[int]], expected: Tuple[bool, List[int]]):
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
