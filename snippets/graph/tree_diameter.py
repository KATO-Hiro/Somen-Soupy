# -*- coding: utf-8 -*-


"""
Usage:

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        ai, bi, ci = map(int, input().split())
        ai -= 1
        bi -= 1

        # ci: cost (non-weighted graph: ci = 1)
        graph[ai].append((ci, bi))
        graph[bi].append((ci, ai))

    tree_diameter = TreeDiameter(vertex_count=n, graph=graph)
    dist, _, _ = tree_diameter.calc(source=0)
"""


class TreeDiameter:
    """Calc distances from start vertex to each vertex in the tree.

    See: https://atcoder.jp/contests/abc361/submissions/55676943
    """

    def __init__(self, vertex_count: int, graph) -> None:
        self.vertex_count = vertex_count
        self.graph = graph

    def calc(self, source: int) -> tuple[int, int, int]:
        assert 0 <= source < self.vertex_count

        p, _ = self._find_farthest_vertex(source=source)
        q, dist_max = self._find_farthest_vertex(source=p)

        return dist_max, p, q

    def _find_farthest_vertex(self, source: int) -> tuple[int, int]:
        from collections import deque

        visited = [False for _ in range(self.vertex_count)]
        que = deque([(0, source)])

        farthest_vertex = source
        dist_max = 0

        while que:
            dist, vertex = que.popleft()

            if visited[vertex]:
                continue

            visited[vertex] = True

            for weight, next_vertex in self.graph[vertex]:
                if not (0 <= next_vertex < self.vertex_count):
                    continue
                if visited[next_vertex]:
                    continue

                new_dist = dist + weight
                que.append((new_dist, next_vertex))

                if new_dist > dist_max:
                    farthest_vertex = next_vertex
                    dist_max = new_dist

        return farthest_vertex, dist_max
