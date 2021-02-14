# -*- coding: utf-8 -*-


def calc_depth(vertex_count: int, graph):
    """Calculates depth of rooted tree.

    Assumption:
        The graph is connected.

    Args:
        vertex_count : The number of vertices in rooted tree.
        graph        : Rooted tree (0-indexed).

    Returns:
        depth : Depth of rooted tree (0-indexed).

    Landau notation: O(|Edges|log|Vertices|).
    """

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


def run_imos(graph, depth, imos):
    """Calculate values of rooted tree faster using imos method.

    Args:
        graph : Rooted tree (0-indexed).
        depth : Depth of rooted tree (0-indexed).
        imos  : List of some values (0-indexed).

    Returns:
        imos  : List of cumulative sum of values (0-indexed).

    Landau notation: O(|Edges|log|Vertices|).
    """

    from collections import deque

    d = deque()
    d.append(0)

    while d:
        vertex = d.popleft()

        for g in graph[vertex]:
            if depth[vertex] < depth[g]:
                imos[g] += imos[vertex]
                d.append(g)

    return imos
