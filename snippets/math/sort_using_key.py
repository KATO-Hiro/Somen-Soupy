# -*- coding: utf-8 -*-

# Usage:
#
#    n = int(input())
#    a = [0] * n
#    b = [0] * n
#
#    for i in range(n):
#        ai, bi = map(int, input().split())
#        a[i] = ai
#        b[i] = bi
#
#    # Sort id based on ai / (ai + bi)
#    ans = sorted(
#        range(1, n + 1),
#        key=lambda i: Fraction(a[i - 1], a[i - 1] + b[i - 1]),
#        reverse=True,
#    )
#
#


# Compare a / b and c / d (= a * d < b * c)
# See:
# https://atcoder.jp/contests/abc308/tasks/abc308_c/editorial
class Fraction:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __lt__(self, other):
        return self.a * other.b < self.b * other.a


# Usage:
#
#    n = int(input())
#    ab = list()
#
#    for i in range(1, n + 1):
#        ai, bi = map(int, input().split())
#        ab.append((ai, bi, i))
#
#    ans = sorted(ab, key=cmp_to_key(compare), reverse=True)

from functools import cmp_to_key
from typing import Literal, Tuple


# See
# https://atcoder.jp/contests/abc308/tasks/abc308_c/editorial
def compare(a: Tuple[int, int, int], b: Tuple[int, int, int]) -> Literal[1, -1, 0]:
    ai, aj, i = a
    bi, bj, j = b
    diff = ai * bj - bi * aj

    if diff > 0:
        return 1
    elif diff < 0:
        return -1
    else:
        return 0
