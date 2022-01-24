# Somen-Soupy

![build](https://github.com/KATO-Hiro/Somen-Soupy/workflows/Python%20package/badge.svg)

Python3 implementation of competitive programming library inspired by spaghetti-source/algorithm.

[日本語のREADME](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/README_ja.md)

## Description

- These are my Python3 implementations of snippets and algorithms, which are written for studying/understanding algorithms.

- These codes are published in __public domain__. You can use the codes for _any purpose without any warranty_.

## Features

- Data Structure
  - [A dequeue that can perform random accesses with O(1)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/data_structure/random_access_deque.py)
  - [Alternatives to ordered set (set) in C++](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/data_structure/deletable_heapq.py)
  - [BIT (Binary Indexed Tree, Fenwick Tree)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/data_structure/bit.py)
  - [Manage two-dimensional lists as one-dimensional lists](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/data_structure/two_dim_list.py)
  - [Segment tree](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/data_structure/segment_tree.py)
  - [Self-balancing binary search tree using pivot values (ordered set in C++)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/data_structure/balancing_tree.py)
  - [The K-th greatest value among the first i terms of P (i = K, K + 1, ..., n)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/data_structure/kth_greatest_value.py)

- DP
  - [LCS (Longest Common Subsequence)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/dp/lcs.py)
  - [LIS (Longest Increasing Subsequence)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/dp/lis.py)

- Graph
  - [BFS (Breadth-First Search) template](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/bfs_template.py)
  - [Dijkstra](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/dijkstra.py)
  - [Rooted Tree](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/rooted_tree.py)
  - [SCC (Strongly Connected Component)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/scc.py)
  - [Tree Distance](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/tree_distance.py)
  - [Union Find Tree](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/unionfind.py)
  - [Union Find Tree (weighted)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/weighted_unionfind.py)
  - [Warshall Floyd](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/warshall_floyd.py)

- Math
  - [Combination](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/combination.py)
  - [Compress coordinate](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/comress.py)
  - [Digit](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/digit.py)
  - [Direct product](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/direct_product.py)
  - [Extended Euclidean algorithm](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/gcd.py)
  - [Factorization](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/factorization.py)
  - [Interger carry](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/carry.py)
  - [Least Common Multiple (LCM)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/lcm.py)
  - [List of indices whose bit is 1](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/bit_index.py)
  - [N-ary number](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/n_ary_number.py)
  - [Pascal's triangle (binomial coefficients, nCr)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/pascals_triangle.py)
  - [Permutation (nPr with mod)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/permutation.py)
  - [Prime](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/prime.py)

- String
  - [To titlecase](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/string/string.py)

## Requirement

### For all users

- Python 3.7.0+, 3.8.0+, 3.9.0+, 3.10.0+
- pip

### For developer

- pytest
- GitHub Actions

## Usage

1. Install this repository by the following method.
2. Search for snippets and algorithms as needed.

## Installation

Paste the following commands at a Terminal prompt.

```terminal
$ git clone https://github.com/KATO-Hiro/Somen-Soupy
```

## References

[Readme Driven Development; RDD](https://qiita.com/b4b4r07/items/c80d53db9a0fd59086ec)

[Software licenses for competitive programming library](https://kimiyuki.net/blog/2020/02/14/licenses-for-kyopro-libraries/)

[spaghetti-source/algorithm](https://github.com/spaghetti-source/algorithm)

[Starting with the Python workflow template](https://docs.github.com/en/actions/guides/building-and-testing-python#starting-with-the-python-workflow-template)
## Author

[@KATO-Hiro](https://twitter.com/k_hiro1818)

## License

[CC0](https://creativecommons.org/share-your-work/public-domain/cc0)
