import pytest

from snippets.graph.cycle_detection import CycleDetection


class TestCycleDetection:
    def test_detect(self) -> None:
        n = 16
        graph = [[] for _ in range(n)]
        # from → to
        directed_graph = [
            [1, 0],
            [0, 2],
            [2, 3],
            [2, 14],
            [3, 5],
            [5, 6],
            [5, 9],
            [6, 7],
            [6, 8],
            [10, 9],
            [9, 11],
            [9, 12],
            [12, 13],
            [12, 15],
            [13, 3],
        ]

        for ai, bi in directed_graph:
            graph[ai].append(bi)

        cd = CycleDetection(graph=graph)
        cycle = cd.detect(is_prohibit_reverse=False)
        cycle_size = len(cycle)

        assert cycle_size == 5
        assert cycle == [3, 5, 9, 12, 13]
