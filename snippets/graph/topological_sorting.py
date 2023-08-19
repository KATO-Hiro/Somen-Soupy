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
    is_DAG, orders = ts.sort_only_reachable_vertices_from(start_id=0)
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

    def sort(self, allow_a_vertex_with_indegree_zero=True) -> Tuple[bool, List[int]]:
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
            if allow_a_vertex_with_indegree_zero and len(que) >= 2:
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

    def sort_only_reachable_vertices_from(
        self, start_id: int = 0
    ) -> Tuple[bool, List[int]]:
        """
        Returns:
            is_DAG: Is it DAG (Directed Acyclic Graph) ?
            orders: Order of vertices (1-indexed).
        """
        is_DAG, orders = self.sort(allow_a_vertex_with_indegree_zero=False)

        if not is_DAG:
            return is_DAG, orders

        que = deque([start_id])
        visited = [False] * self.vertex_count

        while que:
            cur = que.popleft()

            if visited[cur]:
                continue

            visited[cur] = True

            for to in self.graph[cur]:
                if visited[to]:
                    continue

                que.append(to)

        reachable_orders = list()

        for order in orders:
            if visited[order]:
                reachable_orders.append(order + 1)

        return is_DAG, reachable_orders
