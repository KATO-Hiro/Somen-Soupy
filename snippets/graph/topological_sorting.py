# -*- coding: utf-8 -*-

"""
Usage:

    n, m = map(int, input().split())
    ts = TopologicalSorting(n)

    for _ in range(m):
        # vertex ai -> bi.
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        ts.add_edge(frm=ai, to=bi)

    is_DAG, orders = ts.sort()
"""

from collections import deque
from typing import List, Tuple


class TopologicalSorting:
    """
    See:
    https://atcoder.jp/contests/abc291/submissions/39241055
    """

    def __init__(self, vertex_count: int) -> None:
        self.vertex_count = vertex_count
        self.graph = [[] for _ in range(vertex_count)]
        self.indegrees = [0] * vertex_count

    def add_edge(self, frm: int, to: int) -> None:
        """
        Args:
            frm(from) -> to: Vertex number (0-indexed).
        """
        assert 0 <= frm < self.vertex_count
        assert 0 <= to < self.vertex_count

        self.graph[frm].append(to)
        self.indegrees[to] += 1

    def sort(self) -> Tuple[bool, List[int]]:
        """
        Returns:
            is_DAG: Is it DAG (Directed Acyclic Graph) ?
            orders: Order of vertices (0-indexed).
        """
        que = deque([i for i in range(self.vertex_count) if self.indegrees[i] == 0])
        results = list()
        # initial_value = 0  # TODO: Set value if needs.
        # costs = [initial_value] * self.vertex_count

        if len(que) == 0:
            return False, []

        while que:
            # No more than two vertices with indegree 0 are allowed.
            if len(que) >= 2:
                return False, []

            vertex = que.popleft()
            results.append(vertex)

            for to in self.graph[vertex]:
                self.indegrees[to] -= 1

                # Update costs.
                # costs[to] = max(costs[to], costs[vertex] + 1)

                if self.indegrees[to] == 0:
                    que.append(to)

        if len(results) == self.vertex_count:
            return True, results
            # return True, costs
        else:
            return False, []
