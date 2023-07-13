# -*- coding: utf-8 -*-


# Usage:
# n = int(input())

# raq_rsq = RAQ_AND_RSQ_ZERO_INDEXED(n)

# # 0-indexed. [left, right)
# raq_rsq.add(left, right, value)
# raq_rsq.query(left, right, value)

# results = raq_rsq.debug_list()


from typing import Any, List


class RAQ_AND_RSQ:
    """Range Add Query and range Sum Query using BIT

    See:
    https://algo-logic.info/binary-indexed-tree/
    https://tjkendev.github.io/procon-library/python/range_query/rsq_raq_bit.html
    https://github.com/kerroggu/AtCoderLibrary/blob/master/src/BIT(RAdd_RSum).py
    """

    BIT_FIRST, BIT_SECOND = 0, 1

    def __init__(self, size: int) -> None:
        self.size = size
        self.bit: List[List[int]] = [
            [0 for _ in range(self.size + 1)] for _ in range(2)
        ]

    def add(self, left: int, right: int, value: Any) -> None:
        self._add(self.BIT_FIRST, left, -value * (left - 1))
        self._add(self.BIT_FIRST, right, value * (right - 1))
        self._add(self.BIT_SECOND, left, value)
        self._add(self.BIT_SECOND, right, -value)

    def _add(self, bit_id: int, index: int, value: Any) -> None:
        while index <= self.size:
            self.bit[bit_id][index] += value
            index += index & -index

    def query(self, left: int, right: int) -> Any:
        return (
            self._get(self.BIT_SECOND, right - 1) * (right - 1)
            + self._get(self.BIT_FIRST, right - 1)
            - self._get(self.BIT_SECOND, left - 1) * (left - 1)
            - self._get(self.BIT_FIRST, left - 1)
        )

    def _get(self, bit_id: int, index: int):
        summed = 0

        while index:
            summed += self.bit[bit_id][index]
            index -= index & -index

        return summed


class RAQ_AND_RSQ_ZERO_INDEXED(RAQ_AND_RSQ):
    def add(self, left: int, right: int, value: Any) -> None:
        assert 0 <= left <= right <= self.size

        super().add(left + 1, right + 1, value)

    def query(self, left: int, right: int) -> Any:
        assert 0 <= left <= right <= self.size

        return super().query(left + 1, right + 1)

    def debug_list(self) -> List[Any]:
        results: List[int] = [0] * (self.size)

        for i in range(self.size):
            results[i] = self.query(i, i + 1)

        return results
