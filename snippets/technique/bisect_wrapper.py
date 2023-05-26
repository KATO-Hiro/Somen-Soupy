# -*- coding: utf-8 -*-

# Usage:
#
# a = [1, 2, 3, 10, 11]  # Expected to be sorted.

# i, value = bisect_lt(a, x)  # the largest element < x
# i, value = bisect_le(a, x)  # the largest element <= x
# j, value = bisect_gt(a, x)  # the smallest element > x
# j, value = bisect_ge(a, x)  # the smallest element >= x
#
# if i is not None:
#     count = i + 1
#
# if j is not None:
#     count = n - j

from bisect import bisect_left, bisect_right
from typing import List


def bisect_lt(sorted_array: List[int], value: int):
    """Find the largest element < x and its index, or None if it doesn't exist."""

    if sorted_array[0] < value:
        index: int = bisect_left(sorted_array, value) - 1

        return index, sorted_array[index]

    return None, None


def bisect_le(sorted_array: List[int], value: int):
    """Find the largest element <= x and its index, or None if it doesn't exist."""

    if sorted_array[0] <= value:
        index: int = bisect_right(sorted_array, value) - 1

        return index, sorted_array[index]

    return None, None


def bisect_gt(sorted_array: List[int], value: int):
    """Find the smallest element > x and its index, or None if it doesn't exist."""

    if sorted_array[-1] > value:
        index: int = bisect_right(sorted_array, value)

        return index, sorted_array[index]

    return None, None


def bisect_ge(sorted_array: List[int], value: int):
    """Find the smallest element >= x and its index, or None if it doesn't exist."""

    if sorted_array[-1] >= value:
        index: int = bisect_left(sorted_array, value)

        return index, sorted_array[index]

    return None, None
