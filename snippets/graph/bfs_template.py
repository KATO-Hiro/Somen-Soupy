# -*- coding: utf-8 -*-

# Grid ===
from collections import deque
from typing import Any, List, Tuple

h, w = map(int, input().split())
# TODO: Change input format if needs.
grid = [list(input().rstrip()) for _ in range(h)]
sy, sx = 0, 0


def bfs_for_grid(
    grid: List[List[Any]], h: int, w: int, sy: int = 0, sx: int = 0
) -> Tuple[List[List[bool]], List[List[int]]]:
    d = deque()
    d.append((sy, sx))
    visited = [[False] * w for _ in range(h)]
    pending = -1
    dist = [[pending] * w for _ in range(h)]
    dist[sy][sx] = 1  # Initialize
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while d:
        y, x = d.popleft()

        if dist[y][x] == pending:
            continue

        if visited[y][x]:
            continue

        visited[y][x] = True

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                continue
            if visited[ny][nx]:
                continue
            if grid[ny][nx] == "#":
                continue
            if dist[ny][nx] != pending and dist[ny][nx] <= dist[y][x]:
                continue

            dist[ny][nx] = dist[y][x] + 1  # Update ans
            d.append((ny, nx))

    return visited, dist


visited, dist = bfs_for_grid(grid=grid, h=h, w=w, sy=sy, sx=sx)

# ===


# Graph ===

from typing import List, Tuple

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    ai, bi = map(int, input().split())
    ai -= 1
    bi -= 1

    graph[ai].append(bi)
    # graph[bi].append(ai) # non-directed

inf = 10**18


def bfs_for_graph(
    vertex_count: int, graph: List[List[int]], start_id: int
) -> Tuple[List[bool], List[int]]:
    d = deque([start_id])
    visited = [False] * vertex_count
    dist = [inf] * vertex_count
    dist[start_id] = 0

    while d:
        cur = d.pop()

        if visited[cur]:
            continue

        visited[cur] = True

        for to in graph[cur]:
            if visited[to]:
                continue

            d.append(to)
            dist[to] = min(dist[to], dist[cur] + 1)

    return visited, dist


start_id = 0
visited, dist = bfs_for_graph(vertex_count=n, graph=graph, start_id=start_id)
# ===
