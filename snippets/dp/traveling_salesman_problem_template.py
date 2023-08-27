# -*- coding: utf-8 -*-

# Template of traveling salesman problem (TSP)
n = int(input())

# Pre-calculation: distance between two vertices.
inf = 10**18  # min dist
# inf = -10 ** 18 # max dist
dist = [[inf for _ in range(n)] for _ in range(n)]

# dp[s][v]: min cost (max value)
# s: visited vertex sets(binary. visited: 1、not visited: 0)
# v: current vertex
dp = [[inf for _ in range(n)] for _ in range(1 << n)]
# Initialize cost / value.
start_id = 0
dp[1 << start_id][start_id] = 0

for s in range(1 << n):
    for v in range(n):
        # Improvement of time complexity.
        if dp[s][v] == inf:
            continue

        for u in range(n):
            if not ((s >> u) & 1) and dist[v][u] != inf:
                dp[s | 1 << u][u] = min(dp[s | 1 << u][u], dp[s][v] + dist[v][u])
                # dp[s | 1 << u][u] = max(dp[s | 1 << u][u], dp[s][v] + dist[v][u])

# Visited all vertices and return to the start vertex.
ans = dp[(1 << n) - 1][start_id]
