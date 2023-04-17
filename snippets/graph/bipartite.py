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

# results = is_bipartite(start_id=0, graph, colors) 


from typing import List

no_color, black, white = 0, 1, -1
# colors = [no_color] * n


# See:
# https://prd-xxx.hateblo.jp/entry/2017/10/13/004256
def is_bipartite(start_id: int, graph: List[List], colors: List[int]):
    stack = [(start_id, black)]  # vertex, color

    while stack:
        vertex, color = stack.pop()
        colors[vertex] = color

        for to in graph[vertex]:
            if colors[to] == color:
                return False

            if colors[to] == no_color:
                stack.append((to, -color))  # Invert colors.

    return True
