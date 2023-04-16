# -*- coding: utf-8 -*-


from typing import List


# See:
# https://kazun-kyopro.hatenablog.com/entry/ABC/298/B
def rotate_90_degrees_to_right(array: List[List]):
    return [list(ai)[::-1] for ai in zip(*array)]
