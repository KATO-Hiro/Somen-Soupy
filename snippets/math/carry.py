# -*- coding: utf-8 -*-


# Usage:
# n = 10
# digits = [0, 9, 11, 4, 15, 119, 2, 36, 7, 8, 9]
# value = carry(n, digits) # [1, 0, 1, 6, 6, 9, 5, 6, 7, 8, 9]


from typing import List


def carry(n: int, digits: List[int]) -> List[int]:
    '''Integer carry.

    Args:
        n     : Size of digits.
        digits: List of numbers. [0, digit, ..., digit]

    returns: 
        List of numbers.

    Landau notation: O(n)
    '''

    for pos in range(n - 1, 0, -1):
        p, q = divmod(digits[pos], 10)
        digits[pos] = q
        digits[pos - 1] += p
        
    if digits[0] == 0:
        digits = digits[1:]

    return digits 