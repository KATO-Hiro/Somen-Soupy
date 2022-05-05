# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    # TODO: Change input format if needs.
    a = list(map(int, input().split()))
    d = deque()
    # Initialize value(s) for a given interval.
    ans = 0

    # Two-Pointer Technique using deque.
    # See:
    # https://qiita.com/keroru/items/6e0a22e8c9bf2a24dc68
    for ai in a:
        d.append(ai)
        # Update value(s) for a given interal using ai.

        # while d and not (conditon):
        #     di = d.popleft()
            # Update value(s) for a given interal using di.

        # Update ans
        size = len(d)
        # ans =

    print(ans)


if __name__ == "__main__":
    main()
