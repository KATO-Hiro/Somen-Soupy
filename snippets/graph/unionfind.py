# -*- coding: utf-8 -*-

"""Snippets for Union Find.

Available functions:
- find_root     : Follows the chain of parent pointers from number up the tree
                  until it reaches a root element, whose parent is itself.
- get_group_size: Get group size.
- is_same_group : Represents the roots of tree number_x and number_y are in the
                  same group.
- merge_if_needs: Uses find_root to determine the roots of the tree number_x and
                  number_y belong to. If the roots are distinct, the trees are
                  combined by attaching the roots of one to the root of the
                  other.
"""

"""
Usage:

    # 1D
    uf = UnionFind(n)

    uf.is_same_group(ui, vi)
    uf.merge_if_needs(ui, vi)

    uf.find_root(i)
    uf.get_group_size(i)

    roots = uf.get_roots()
    edge_count = uf.get_edge_count(i)
    group_count = uf.get_group_count()


    # 2D
    h, w = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    uf = UnionFind2D(height=h, width=w)

    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                continue

            if (i + 1 < h) and s[i + 1][j] == ".":
                uf.merge_if_needs(j, i, j, i + 1)
            if (j + 1 < w) and s[i][j + 1] == ".":
                uf.merge_if_needs(j, i, j + 1, i)

    uf.is_same_group(w1, h1, w2, h2)
    uf.merge_if_needs(w1, h1, w2, h2)

    uf.find_root(w1, h1)
    uf.get_group_size(w1, h1)

    roots = uf.get_roots()
    edge_count = uf.get_edge_count(w1, h1)
    group_count = uf.get_group_count()
"""

from typing import List


class UnionFind:
    """Represents a data structure that tracks a set of elements partitioned
       into a number of disjoint (non-overlapping) subsets.

    Landau notation: O(α(n)), where α(n) is the inverse Ackermann function.

    See:
    https://www.youtube.com/watch?v=zV3Ul2pA2Fw
    https://en.wikipedia.org/wiki/Disjoint-set_data_structure
    https://atcoder.jp/contests/abc120/submissions/4444942
    https://atcoder.jp/contests/abc292/submissions/39410075
    """

    def __init__(self, number_count: int) -> None:
        """
        Args:
            number_count: The size of elements (greater than 2).
        """
        self.parent_numbers = [-1 for _ in range(number_count)]
        self.edge_count = [0 for _ in range(number_count)]
        self.group_count = number_count

    def find_root(self, number: int) -> int:
        """Follows the chain of parent pointers from number up the tree until
           it reaches a root element, whose parent is itself.
        Args:
            number: The trees id (0-index).

        Returns:
            The index of a root element.
        """
        if self.parent_numbers[number] < 0:
            return number

        self.parent_numbers[number] = self.find_root(self.parent_numbers[number])
        return self.parent_numbers[number]

    def get_group_size(self, number: int) -> int:
        """
        Args:
            number: The trees id (0-index).

        Returns:
            The size of group.
        """
        return -self.parent_numbers[self.find_root(number)]

    def is_same_group(self, number_x: int, number_y: int) -> bool:
        """Represents the roots of tree number_x and number_y are in the same
           group.
        Args:
            number_x: The trees x (0-index).
            number_y: The trees y (0-index).
        """
        return self.find_root(number_x) == self.find_root(number_y)

    def merge_if_needs(self, number_x: int, number_y: int) -> bool:
        """Uses find_root to determine the roots of the tree number_x and
           number_y belong to. If the roots are distinct, the trees are combined
           by attaching the roots of one to the root of the other.
        Args:
            number_x: The trees x (0-index).
            number_y: The trees y (0-index).
        """
        x = self.find_root(number_x)
        y = self.find_root(number_y)

        self.edge_count[x] += 1

        if x == y:
            return False

        self.group_count -= 1

        if self.parent_numbers[x] > self.parent_numbers[y]:
            x, y = y, x

        self.parent_numbers[x] += self.parent_numbers[y]
        self.parent_numbers[y] = x
        self.edge_count[x] += self.edge_count[y]
        return True

    def get_roots(self) -> List[int]:
        return [i for i, x in enumerate(self.parent_numbers) if x < 0]

    def get_edge_count(self, number: int) -> int:
        return self.edge_count[number]

    def get_group_count(self) -> int:
        return self.group_count


class UnionFind2D:
    """Extends UnionFind to two dimensions.

    See:
    https://atcoder.jp/contests/past202010-open/submissions/21472171
    """

    def __init__(self, height: int, width: int) -> None:
        self.height: int = height
        self.width: int = width
        self.size: int = height * width
        self.uf: UnionFind = UnionFind(self.size)

    def find_root(self, x: int, y: int) -> int:
        assert 0 <= x < self.width
        assert 0 <= y < self.height

        return self.uf.find_root(self._to_number(x, y))

    def get_group_size(self, x: int, y: int) -> int:
        assert 0 <= x < self.width
        assert 0 <= y < self.height

        return self.uf.get_group_size(self._to_number(x, y))

    def is_same_group(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        assert 0 <= x1 < self.width
        assert 0 <= y1 < self.height
        assert 0 <= x2 < self.width
        assert 0 <= y2 < self.height

        return self.find_root(x1, y1) == self.find_root(x2, y2)

    def merge_if_needs(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        assert 0 <= x1 < self.width
        assert 0 <= y1 < self.height
        assert 0 <= x2 < self.width
        assert 0 <= y2 < self.height

        return self.uf.merge_if_needs(self._to_number(x1, y1), self._to_number(x2, y2))

    def get_roots(self) -> List[int]:
        return self.uf.get_roots()

    def get_edge_count(self, x: int, y: int) -> int:
        assert 0 <= x < self.width
        assert 0 <= y < self.height

        return self.uf.get_edge_count(self._to_number(x, y))

    def get_group_count(self) -> int:
        return self.uf.get_group_count()

    def _to_number(self, x: int, y: int) -> int:
        """
        Args:
            x, y: Coordinates in grid (0-index).

        Returns:
            The trees id (0-index).
        """
        return x + self.width * y
