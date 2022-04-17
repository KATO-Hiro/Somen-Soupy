# -*- coding: utf-8 -*-


"""
Usage:

    point1, point2 = (0, 0), (2, 6)
    result = calc_line_passing_through(point1, point2)
"""


def calc_line_passing_through(point1, point2):
    '''

    Args:
        point1, point2: Points that constitutes a line.

    Returns:
        parameters of the line.
            slope    : a, b
            intercept: c

    Landau notation: O(log(min(a, b, c))).

    See:
    https://atcoder.jp/contests/abc248/submissions/31018608
    '''

    from math import gcd

    a = point2[1] - point1[1]
    b = point1[0] - point2[0]
    c = -(point1[0] * a + point1[1] * b)

    if a < 0:
        a, b, c = -a, -b, -c

    if a == 0 and b < 0:
        b, c = -b, -c

    g = gcd(gcd(a, b), c)
    a //= g
    b //= g
    c //= g

    return (a, b, c)
