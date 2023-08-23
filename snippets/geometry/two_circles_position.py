# -*- coding: utf-8 -*-


"""
Usage:

    result = is_on_circle(xi, yi, ri, x, y)

    result = is_hit(xi, yi, ri, xj, yj, rj)
    result = is_intersected(xi, yi, ri, xj, yj, rj)
"""


from enum import Enum, auto


# See:
# https://docs.python.org/ja/3/howto/enum.html
class TwoCirclesPosition(Enum):
    Inside = auto()
    Inscribed = auto()
    Intersect = auto()
    Circumscribed = auto()
    Outside = auto()


def is_hit(xi, yi, ri, xj, yj, rj) -> bool:
    result = is_intersected(xi, yi, ri, xj, yj, rj)

    if result in [
        TwoCirclesPosition.Inscribed,
        TwoCirclesPosition.Intersect,
        TwoCirclesPosition.Circumscribed,
    ]:
        return True
    else:
        return False


# See:
# https://www.mathlion.jp/article/ar131.html
def is_intersected(xi: int, yi: int, ri: int, xj: int, yj: int, rj: int):
    dist = abs(xi - xj) ** 2 + abs(yi - yj) ** 2

    if rj > ri:
        ri, rj = rj, ri

    if (ri - rj) ** 2 > dist:
        return TwoCirclesPosition.Inside
    if (ri - rj) ** 2 == dist:
        return TwoCirclesPosition.Inscribed
    elif (ri - rj) ** 2 < dist < (ri + rj) ** 2:
        return TwoCirclesPosition.Intersect
    elif dist == (ri + rj) ** 2:
        return TwoCirclesPosition.Circumscribed
    elif dist > (ri + rj) ** 2:
        return TwoCirclesPosition.Outside


def is_on_circle(xi: int, yi: int, ri: int, x: int, y: int) -> bool:
    if (x - xi) ** 2 + (y - yi) ** 2 == ri**2:
        return True
    else:
        return False
