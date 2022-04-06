
# -*- coding: utf-8 -*-


"""
Usage:

    n, m = map(int, input().split())
    edges = list()

    for i in range(m):
        ai, bi, ci = map(int, input().split())
        ai -= 1
        bi -= 1
        edges.append((ci, ai, bi))  # (cost, vertex_start, vertex_end)

    # Calc reachable vertices using by BFS or DFS.
    reachables = [False] * n

    has_cycle, dist = bellman_ford(n, edges, reachables)
"""


def bellman_ford(
    vertex_count: int,
    edges,
    reachables=None,
    dist_max: int = 10 ** 18,
    source: int = 0
):
    """Uses Bellman Ford algorithm to find the shortest path in a graph.

    Args:
        vertex_count: The number of vertices.
        edges       : List of (cost, vertex_start, vertex_end) (0-indexed).
        reachables  : List of reachable vertices.
        dist_max    : The maximum distance (= inf).
        source      : Vertex number (0-indexed).

    Returns:
        has_cycle: Negative cycle or not.
        dist  : List of the shortest distance.

    Landau notation: O(Edges・Vertices).

    See:
    https://www.youtube.com/watch?v=1Z6ofKN03_Y
    https://blog.hamayanhamayan.com/entry/2017/05/14/134606
    """

    dist = [dist_max] * vertex_count
    dist[source] = 0

    if reachables is None:
        reachables = [True] * vertex_count

    is_updated = True
    step_count = 0
    has_cycle = False

    while is_updated:
        is_updated = False

        for ci, ai, bi in edges:
            if not reachables[ai] or not reachables[bi]:
                continue

            new_cost = dist[ai] + ci

            if new_cost < dist[bi]:
                dist[bi] = new_cost
                is_updated = True

        step_count += 1

        if step_count > vertex_count:
            has_cycle = True
            break

    return has_cycle, dist
