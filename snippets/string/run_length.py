# -*- coding: utf-8 -*-

"""
Usage:
s = ["a", "a", "a", "b", "c", "c", "c", "c", "d", "d"]
results = run_length_encoding(s)
print(results)  # [["a", 3], ["b", 1], ["c", 4], ["d", 2]]

t = [["a", 3], ["b", 1], ["c", 4], ["d", 2]]
results = run_length_decoding(t)
print(results)  # "aaabccccdd"
"""


from typing import List


def run_length_encoding(iterable: list) -> List[list]:
    '''
    Args:
        iterable: A list of numbers or strings.

    Returns:
        A list containing consecutive characters and their count.

    See:
    https://qiita.com/DaikiSuyama/items/07e237b7372e7c7b3432
    '''

    from itertools import groupby

    results = [[key, len(list(group))] for key, group in groupby(iterable)]

    return results


def run_length_decoding(list: List[list]) -> str:
    '''
    Args:
        A list containing consecutive characters and their count.

    Returns:
        iterable: A string of numbers or strings.

    See:
    https://qiita.com/Kept1994/items/e9179d1dd7c6455d6883
    '''

    results = ""

    for key, value in list:
        results += str(key) * value

    return results
