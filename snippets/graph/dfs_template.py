# -*- coding: utf-8 -*-


def main():
    import sys
    from functools import lru_cache

    sys.setrecursionlimit(10**8)

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    @lru_cache(maxsize=None)
    def dfs(cur, parent=-1):
        # Base case
        # if codition:
        #     return initial_value  # TODO: Update value.

        # Rec case
        value_min = 10**18  # TODO: Initialize value.
        value_max = 0  # TODO: Initialize value.

        for to in graph[cur]:
            if to == parent:
                continue

            # preorder
            # TODO: Update value.

            result = dfs(to, cur)

            # postorder
            # TODO: Update value.

        return  # value  # TODO: Update value.

    print(dfs(0))


if __name__ == "__main__":
    main()
