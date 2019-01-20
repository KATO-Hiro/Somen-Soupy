# -*- coding: utf-8 -*-
'''Snippets for combination.

Available functions:
- count_combination: Count the total number of combinations.
'''


def count_combination(n: int, r: int, mod: int = 10 ** 9 + 7) -> int:
    '''Count the total number of combinations.
        nCr % mod.

    Args:
        n   : Elements. Int of number (greater than 1).
        r   : The number of r-th combinations. Int of number (greater than 0).
        mod : Modulo. The default is 10 ** 9 + 7.

    Returns:
        The total number of combinations.

    Landau notation: O(n)

    See:
    https://qiita.com/derodero24/items/91b6468e66923a87f39f
    '''

    if r > (n - r):
        return count_combination(n, n - r)

    if r == 0 or r == n:
        return 1

    if r == 1:
        return n

    multiple = 1
    division = 1

    for i in range(r):
        multiple *= n - i
        division *= i + 1
        multiple %= mod
        division %= mod

    return multiple * pow(division, mod - 2, mod) % mod
