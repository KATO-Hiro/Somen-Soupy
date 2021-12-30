# -*- coding: utf-8 -*-

# Usage:
#
#    h, w = map(int, input().split())
#    td = TwoDimList(h, w)
#
#    td.plus(ai, bi, 1) # array[ai][bi] += 1
#    td.insert(ai, bi, x) # array[ai][bi] = x
#    td.read(ai, bi) # array[ai][bi]


class TwoDimList:
    """Manage two-dimensional lists as one-dimensional lists.

    See:
    https://atcoder.jp/contests/typical90/submissions/23891910
    """

    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.arr = [0] * (self.h * self.w)

    def read(self, hi, wi):
        return self.arr[self.w * hi + wi]

    def insert(self, hi, wi, value):
        self.arr[hi * self.w + wi] = value

    def plus(self, hi, wi, value):
        self.arr[hi * self.w + wi] += value
