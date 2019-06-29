# -*- coding: utf-8 -*-
import pytest

from snippets.graph.unionfind import UnionFind


class TestUnionFind(object):

    def test_find_root(self):
        number = 5
        uf = UnionFind(number)

        actual = uf.find_root(0)
        expected = 0
        assert actual == expected

        # Merge element 0, 1, 2.
        uf.merge_if_needs(0, 1)
        uf.merge_if_needs(0, 2)
        actual = uf.find_root(2)
        expected = 0
        assert actual == expected

    def test_get_group_size(self):
        number = 5
        uf = UnionFind(number)

        actual = uf.get_group_size(0)
        expected = 1
        assert actual == expected

        # Merge element 0 and 1.
        uf.merge_if_needs(0, 1)
        actual = uf.get_group_size(0)
        expected = 2
        assert actual == expected

    def test_is_same_group(self):
        number = 5
        uf = UnionFind(number)

        actual = uf.is_same_group(0, 1)
        expected = False
        assert actual == expected

        actual = uf.is_same_group(0, 2)
        expected = False
        assert actual == expected

        # Merge element 0, 1.
        uf.merge_if_needs(0, 1)
        actual = uf.is_same_group(0, 1)
        expected = True
        assert actual == expected

        # Element 0 and 2 are not the same group.
        actual = uf.is_same_group(0, 2)
        expected = False
        assert actual == expected
