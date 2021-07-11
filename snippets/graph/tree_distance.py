# -*- coding: utf-8 -*-


"""
Usage:

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    
    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai].append(bi)
        graph[bi].append(ai)

    td = TreeDistance(n, graph)
    dist = td.calc()
"""


class TreeDistance:
    """Calc distances from start vertex to each vertex in the tree.

    See:
    """

    def __init__(self, vertex_count, graph) -> None:
        self.dist = [0 for _ in range(vertex_count)]
        self._graph = graph
        self._visited = [False for _ in range(vertex_count)]

    def calc(self, start_vertex=0):
        self._bfs(start_vertex)

        return self.dist

    def _bfs(self, vertex):
        from collections import deque

        d = deque()
        d.append(vertex)
        self._visited[vertex] = True

        while d:
            di = d.popleft()

            for to in self._graph[di]:
                if self._visited[to]:
                    continue

                self._visited[to] = True
                self.dist[to] = self.dist[di] + 1
                d.append(to)
