# -*- coding: utf-8 -*-


def count_digit(max_number: int) -> int:
    '''
    Args:
        max_number: Int of number (greater than 1).

    Returns:
        the number of digit.

    Landau notation: O(log n)
    '''
    if max_number == 0:
        return 1

    digit = 0

    while max_number:
        digit += 1
        max_number //= 10

    return digit
