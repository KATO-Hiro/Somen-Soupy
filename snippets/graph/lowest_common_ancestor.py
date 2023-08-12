# -*- coding: utf-8 -*-


# Verified
# https://atcoder.jp/contests/codequeen2023-final-open/submissions/44446373

# Usage

# n = int(input())
# graph = [[] for _ in range(n)]

# for _ in range(n - 1):
#     ai, bi = map(int, input().split())
#     ai -= 1
#     bi -= 1

#     graph[ai].append(bi)
#     graph[bi].append(ai)

# 0-indexed
# root = 0
# tree = LowestCommonAncestor(graph=graph, root=root)
# lca = tree.lca(ui, vi)
# dist = tree.calc_dist(ui, vi)
# result = tree.is_on_path(ui, vi, ai)

from typing import List


# See:
# https://ikatakos.com/pot/programming_algorithm/graph_theory/lowest_common_ancestor
# https://atcoder.jp/contests/codequeen2023-final-open/submissions/44445587
class LowestCommonAncestor:
    def __init__(self, graph: List[List[int]], root=0) -> None:
        n = len(graph)
        k = n.bit_length()
        PENDING = -1

        # parent[k][u] := 2 ** k ahead of u.
        parent: List[List[int]] = [[PENDING] * n for _ in range(k)]
        depth: List[int] = [PENDING] * n
        depth[root] = 0
        stack: List[int] = [root]

        while stack:
            u = stack.pop()

            for v in graph[u]:
                if depth[v] != PENDING:
                    continue

                depth[v] = depth[u] + 1
                parent[0][v] = u
                stack.append(v)

        for ki in range(k - 1):
            for u in range(n):
                if parent[ki][u] < 0:
                    parent[ki + 1][u] = -1
                else:
                    parent[ki + 1][u] = parent[ki][parent[ki][u]]

        self.n: int = n
        self.k: int = k
        self.parent: List[List[int]] = parent
        self.depth: List[int] = depth

    def lca(self, u: int, v: int) -> int:
        assert 0 <= u < self.n
        assert 0 <= v < self.n

        depth, parent = self.depth, self.parent

        if depth[u] < depth[v]:
            u, v = v, u

        for ki in range(self.k):
            if (depth[u] - depth[v]) >> ki & 1:
                u = parent[ki][u]

        if u == v:
            return u

        for ki in range(self.k - 1, -1, -1):
            if parent[ki][u] != parent[ki][v]:
                u = parent[ki][u]
                v = parent[ki][v]

        return parent[0][u]

    def calc_dist(self, u: int, v: int) -> int:
        assert 0 <= u < self.n
        assert 0 <= v < self.n

        return self.depth[u] + self.depth[v] - 2 * self.depth[self.lca(u, v)]

    def is_on_path(self, u: int, v: int, a: int) -> bool:
        assert 0 <= u < self.n
        assert 0 <= v < self.n
        assert 0 <= a < self.n

        return self.calc_dist(u, a) + self.calc_dist(a, v) == self.calc_dist(u, v)
