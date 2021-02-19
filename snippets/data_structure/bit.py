# -*- coding: utf-8 -*-


# Usage:
# n = int(input())
# bit = BIT(n)
# bit.add(index, value)
# bit.sum(index)


class BIT:
    """Binary Indexed Tree (Fenwick Tree)

    Args:
        size: List size (greater than 0).

    """

    def __init__(self, size: int):
        self.size = size
        self._bit = [0 for _ in range(self.size + 1)]

    def add(self, index: int, value: int) -> None:
        """Adds value to list with index i.

        Args:
            index: The number of index (1-indexed).
            value: A value

        Landau notation: O(log n)
        """

        while index <= self.size:
            self._bit[index] += value
            index += index & -index

    def sum(self, index) -> int:
        """Calculate the sum of elements from 1 to index.

        Args:
            index: The number of index (1-indexed).

        Returns:
            The sum of elements from 1 to index.

        Landau notation: O(log n)
        """

        summed = 0

        while index > 0:
            summed += self._bit[index]
            index -= index & -index

        return summed
