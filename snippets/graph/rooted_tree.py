# -*- coding: utf-8 -*-


def calc_depth(vertex_count: int, graph):
    from collections import deque

    PENDING = -1
    depth = [PENDING for _ in range(vertex_count)]
    parent = [PENDING for _ in range(vertex_count)]
    depth[0], parent[0] = 0, 0
    d = deque()
    d.append(0)

    while d:
        vertex = d.popleft()

        for g in graph[vertex]:
            if depth[g] == PENDING:
                depth[g] = depth[vertex] + 1
                parent[g] = vertex
                d.append(g)

    return depth
