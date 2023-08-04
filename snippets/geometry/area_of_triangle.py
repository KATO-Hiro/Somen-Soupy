# -*- coding: utf-8 -*-

"""
Usage:

point1 = x1, y1
point2 = x2, y2
point3 = x3, y3

area = result = calc_area_of_triangle(point1, point2, point3)
print(area)
"""


from typing import Tuple


def calc_area_of_triangle(
    point1: Tuple[int, int], point2: Tuple[int, int], point3: Tuple[int, int]
) -> float:
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3

    area = abs((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)) / 2

    return area
