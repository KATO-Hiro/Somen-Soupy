# -*- coding: utf-8 -*-


"""
Usage:

array = [3, 6, 7, 2, 5, 5, 1, 10, 8, 5]

# Initialize
O(N)
finder = Finder(array)
finder = Finder(array, offset=-100)

finders = [Finder() for _ in range(10)]

## Manual initialization
for finder in finders:
    finder.init(array)
    finder.init(array, offset=-100)

# Add and remove elements
finder.append(11)
finder.append_list([12, 13, 14])

finder.pop()
finder.clear()

# Find index(es)
## Input and output are expected to be 0-indexed
## -1: not found
index = finder.find_index(5, 0)  # 4
index = finder.find_index(5, 1)  # 5
index = finder.find_index(5, 2)  # 9
index = finder.find_index(5, 3)  # -1
index = finder.find_index(11, 0)  # -1

indexes = finder.find_indexes(2)  # [3]
indexes = finder.find_indexes(5)  # [4, 5, 9]
indexes = finder.find_indexes(11)  # [-1]

index = finder.find_next_index(4, 5)  # 5
index = finder.find_next_index(5, 5)  # 9
index = finder.find_next_index(9, 5)  # -1

index = finder.find_prev_index(4, 5)  # -1
index = finder.find_prev_index(5, 5)  # 4
index = finder.find_prev_index(9, 5)  # 5

index = finder.find_ceil_index(3, 5)  # 4
index = finder.find_ceil_index(4, 5)  # 4
index = finder.find_ceil_index(5, 5)  # 5
index = finder.find_ceil_index(9, 5)  # 9

index = finder.find_floor_index(3, 5)  # -1
index = finder.find_floor_index(4, 5)  # 4
index = finder.find_floor_index(5, 5)  # 5
index = finder.find_floor_index(9, 5)  # 9

index = finder.find_cycle_next_index(5, 5)  # 9
index = finder.find_cycle_next_index(9, 5)  # 4
index = finder.find_cycle_next_index(11, 0)  # -1

index = finder.find_cycle_prev_index(4, 5)  # 9
index = finder.find_cycle_prev_index(5, 5)  # 4

index = finder.find_cycle_ceil_index(5, 5)  # 5
index = finder.find_cycle_ceil_index(9, 5)  # 9

index = finder.find_cycle_floor_index(4, 5)  # 4
index = finder.find_cycle_floor_index(5, 5)  # 5

# Count values in ranges [left, right]
count = finder.count_values_in_ranges(5, 4, 8)  # 2
count = finder.count_values_in_ranges(5, 4, 9)  # 3
count = finder.count_values_in_ranges(11, 0, 9)  # 0

# Getter
result = finder.is_empty()  # False
size = finder.get_size()  # 10
"""

# See:
# Original source: https://atcoder.jp/contests/abc367/submissions/56800083
# Translate C++ to Python

from bisect import bisect_left, bisect_right
from typing import Generic, List, TypeVar

T = TypeVar("T", bound=List[int])

NOT_FOUND = -1


class Finder(Generic[T]):
    def __init__(self, values: T = [], offset: int = 0) -> None:
        self.values = values
        self.offset = offset
        self.indexes = []

        if values:
            self.init(values, offset)

    def init(self, values: T, offset: int = 0) -> None:
        self.values = values
        self.offset = offset

        if not self.values:
            return None

        value_min, value_max = min(values), max(values)
        inf = offset + 10**12
        assert offset <= value_min and value_max < inf
        self.indexes = [[] for _ in range(value_max - offset + 1)]

        for i in range(len(self.values)):
            self.find_indexes(self.values[i]).append(i)

    def append_list(self, values: T) -> None:
        for value in values:
            self.append(value)

    def append(self, value: int) -> None:
        assert self.offset <= value

        if len(self.indexes) <= value - self.offset:
            self.indexes.extend(
                [[] for _ in range(value - self.offset - len(self.indexes) + 1)]
            )
        self.find_indexes(value).append(self.get_size())
        self.values.append(value)

    def pop(self) -> int | None:
        if self.is_empty():
            return None

        self.find_indexes(self.values[-1]).pop()

        return self.values.pop()

    def clear(self) -> None:
        self.values.clear()
        self.indexes.clear()

    def find_indexes(self, value: int) -> List[int]:
        if self._validate_range(value):
            return [NOT_FOUND]

        return self.indexes[value - self.offset]

    def find_index(self, value: int, right: int) -> int:
        if self._validate_range(value):
            return NOT_FOUND

        indexes = self.find_indexes(value)

        return NOT_FOUND if len(indexes) <= right else indexes[right]

    def find_next_index(self, index: int, value: int) -> int:
        if self._validate_range(value):
            return NOT_FOUND

        indexes = self.find_indexes(value)
        pos = bisect_right(indexes, index)

        return NOT_FOUND if pos == len(indexes) else indexes[pos]

    def find_prev_index(self, index: int, value: int) -> int:
        if self._validate_range(value):
            return NOT_FOUND

        indexes = self.find_indexes(value)
        pos = bisect_left(indexes, index)

        return NOT_FOUND if pos == 0 else indexes[pos - 1]

    def find_ceil_index(self, index: int, value: int) -> int:
        return self.find_next_index(index - 1, value)

    def find_floor_index(self, index: int, value: int) -> int:
        return self.find_prev_index(index + 1, value)

    def find_cycle_next_index(self, index: int, value: int) -> int:
        if self._validate_range(value):
            return NOT_FOUND

        next_index = self.find_next_index(index, value)

        if next_index == NOT_FOUND:
            next_index = self.find_next_index(-1, value)

        return next_index

    def find_cycle_prev_index(self, index: int, value: int) -> int:
        if self._validate_range(value):
            return NOT_FOUND

        prev_index = self.find_prev_index(index, value)

        if prev_index == NOT_FOUND:
            prev_index = self.find_prev_index(self.get_size(), value)

        return prev_index

    def find_cycle_ceil_index(self, index: int, value: int) -> int:
        return self.find_cycle_next_index(index - 1, value)

    def find_cycle_floor_index(self, index: int, value: int) -> int:
        return self.find_cycle_prev_index(index + 1, value)

    def count_values_in_ranges(self, value: int, left: int, right: int) -> int:
        return self._count_value(right, value) - self._count_value(left - 1, value)

    def is_empty(self) -> bool:
        return not self.values

    def get_size(self) -> int:
        return len(self.values)

    def _validate_range(self, value: int) -> bool:
        return value < self.offset or self.offset + len(self.indexes) <= value

    def _count_value(self, right: int, value: int) -> int:
        if self._validate_range(value):
            return 0

        indexes = self.find_indexes(value)

        return bisect_right(indexes, right)
