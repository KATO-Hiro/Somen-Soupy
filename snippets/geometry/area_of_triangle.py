# -*- coding: utf-8 -*-


from typing import Tuple


def calc_area_of_triangle(
    point1: Tuple[int, int], point2: Tuple[int, int], point3: Tuple[int, int]
) -> float:
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3

    area = abs((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)) / 2

    return area
