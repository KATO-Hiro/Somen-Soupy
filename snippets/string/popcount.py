# -*- coding: utf-8 -*-


def popcount(n: int) -> int:
    '''Count set bits in an integer.

    Args:
        n: Int of number (greater than 0).

    Returns:
        The number of set bits.

    Landau notation: O(log n)

    See:
    https://www.geeksforgeeks.org/count-set-bits-in-an-integer/
    '''

    return bin(n).count("1")
