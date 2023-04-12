# -*- coding: utf-8 -*-

from snippets.data_structure.trie_tree import TrieTree


class TestTrieTree:
    def test_calc_longest_common_prefix_count(self):
        s = ["abracadabra", "bracadabra", "racadabra", "acadabra", "cadabra", "adabra", "dabra", "abra", "bra", "ra", "a"]
        t = TrieTree()

        for si in s:
            t.insert(si)

        actual = list()
        expected = [4, 3, 2, 1, 0, 1, 0, 4, 3, 2, 1]

        for si in s:
            result = t.calc_longest_common_prefix_count(si)
            actual.append(result)
        
        assert actual == expected
