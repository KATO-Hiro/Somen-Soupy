# -*- coding: utf-8 -*-

# Usage:
#
# n, m = map(int, input().split())
# graph = [[] for _ in range(n)]

# for _ in range(m):
#     ai, bi = map(int, input().split())
#     ai -= 1
#     bi -= 1

#     graph[ai].append(bi)
#     graph[bi].append(ai)

# for i in range(n):
#     if colors[i] != no_color:
#         continue

#     flag, black_count, white_count = is_bipartite(start_id=i, graph=graph, colors=colors)

#     if flag:
#         print(black_count, white_count)
#     else:
#         print(0) # Impossible

from typing import List, Tuple

no_color, black, white = 0, 1, -1
# colors = [no_color] * n


# See:
# https://prd-xxx.hateblo.jp/entry/2017/10/13/004256
def is_bipartite(
    start_id: int,
    graph: List[List],
    colors: List[int],
    black_count: int = 0,
    white_count: int = 0,
) -> Tuple[bool, int, int]:
    stack = [(start_id, black)]  # vertex, color

    while stack:
        vertex, color = stack.pop()

        if colors[vertex] != no_color:
            continue

        colors[vertex] = color

        if color == black:
            black_count += 1
        elif color == white:
            white_count += 1

        for to in graph[vertex]:
            if colors[to] == color:
                return False, 0, 0

            if colors[to] == no_color:
                stack.append((to, -color))  # Invert colors.

    return True, black_count, white_count
