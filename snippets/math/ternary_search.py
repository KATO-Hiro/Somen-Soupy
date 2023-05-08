# -*- coding: utf-8 -*-


# Define function shape.
def f(value):
    return value


def ternary_search():
    lower = 0  # TODO: Change lower value if necessary.
    upper = 10 ** 18  # TODO: Change upper value if necessary.

    while lower + 2 < upper:
        left_center = (2 * lower + upper) // 3
        right_center = (lower + 2 * upper) // 3

        # >: min value, <: max value
        if f(left_center) > f(right_center):
            lower = left_center
        else:
            upper = right_center

    # Search for a range of integers if necessary.
    ans = float("inf")

    for i in range(max(1, int(lower - 5)), int(upper) + 5):
        ans = min(ans, f(i))

    print(ans)
