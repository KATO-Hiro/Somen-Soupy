# -*- coding: utf-8 -*-

# Usage:
#
#    n = int(input())
#    s = [input().rstrip() for _ in range(n)]
#    t = TrieTree()
#
#    for si in s:
#        t.insert(si)
#
#    for si in s:
#        t.calc_longest_common_prefix_count(si)


class TrieTree:
    '''

    See:
    https://atcoder.jp/contests/abc287/submissions/38393825
    '''
    def __init__(self) -> None:
        self.tree = {}
        self.count = 0

    def insert(self, word: str) -> None:
        node = self

        for character in word:
            node.count += 1

            if character not in node.tree:
                node.tree[character] = TrieTree()

            node = node.tree[character]

        node.count += 1

    def calc_longest_common_prefix_count(self, word: str) -> int:
        node = self
        ans = 0

        for character in word:
            node = node.tree[character]

            if node.count == 1:
                break

            ans += 1

        return ans
