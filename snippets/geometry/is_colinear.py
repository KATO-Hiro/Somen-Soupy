# -*- coding: utf-8 -*-


"""
Usage:

    point = (1, 3)
    point1, point2 = (0, 0), (2, 6)
    result = is_colinear(point, point1, point2)
"""


def is_colinear(point, point1, point2) -> bool:
    """Determine if a point is colinear.

    Args:
        point: Tuple of x, y.
        point1, point2: Points that constitutes a line.

    Returns:
        bool: True if point is colinear between point1 and point2.

    Landau notation: O(1).

    See:
    https://atcoder.jp/contests/abc248/tasks/abc248_e/editorial
    """

    x, y = point
    x1, y1 = point1
    x2, y2 = point2

    result1 = (x2 - x1) * (y - y1)
    result2 = (y2 - y1) * (x - x1)

    return result1 == result2
