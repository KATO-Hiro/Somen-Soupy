# -*- coding: utf-8 -*-

"""
Usage:

sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    ai, bi = map(int, input().split())
    ai -= 1
    bi -= 1

    graph[ai].append(bi)
    # graph[bi].append(ai)  # Non-Directed

cd = CycleDetection(graph=graph)
results = cd.detect(is_prohibit_reverse=False)
# results = cd.detect()  # Non-Directed

print(len(results))  # Size
print(*map(lambda x: x + 1, results))  # 1-indexed.
"""

from typing import Any, List, Tuple


# See:
# https://drken1215.hatenablog.com/entry/2023/05/20/200517
class CycleDetection:
    pending: int = -1

    def __init__(self, graph: List[List[int]]) -> None:
        self.vertex_count: int = len(graph)
        self.graph: List[List[int]] = graph
        self.seen: List[bool] = [False] * self.vertex_count
        self.finished: List[bool] = [False] * self.vertex_count
        self.history: List[Any] = []

    def detect(self, is_prohibit_reverse: bool = True) -> List[Any]:
        pos = self.pending

        for vertex in range(self.vertex_count):
            if self.seen[vertex]:
                continue

            self.history.clear()
            pos = self._dfs(vertex, self.pending, is_prohibit_reverse)

            if pos != self.pending:
                return self._reconstruct(pos)

        return []

    def _reconstruct(self, pos: int) -> List[int]:
        cycle: List[Any] = []

        while self.history:
            cur = self.history.pop()
            cycle.append(cur)

            if cur == pos:
                break

        return cycle[::-1]

    def _dfs(self, cur: int, parent: int, is_prohibit_reverse: bool = True) -> int:
        self.seen[cur] = True
        self.history.append(parent)

        for to in self.graph[cur]:
            if is_prohibit_reverse and (to == parent):
                continue
            if self.finished[to]:
                continue

            # Detected cycle.
            if self.seen[to] and not self.finished[to]:
                self.history.append(cur)
                return to

            pos = self._dfs(to, cur, is_prohibit_reverse)

            if pos != self.pending:
                return pos

        self.finished[cur] = True
        self.history.pop()
        return self.pending
