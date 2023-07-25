# Somen-Soupy

![build](https://github.com/KATO-Hiro/Somen-Soupy/workflows/Python%20package/badge.svg)

## 説明

- 競技プログラミングのコンテストで使用するスニペットやアルゴリズムがPython3で実装されています。

## 主な機能

- 幾何
  - [線分の傾き・切片を求める](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/geometry/line_passing_through_points.py)
  - [点が線分上にあるかを判定](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/geometry/is_colinear.py)

- グラフ理論
  - [木: 任意の頂点から各頂点への距離を求める (各リンクの長さが1の場合)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/tree_distance.py)
  - [強連結成分分解 (SCC)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/scc.py)
  - [有向・無向グラフのサイクル検出・復元(最初の1つのみ)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/cycle_detection.py)
  - [ダイクストラ法](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/dijkstra.py)
  - [トポロジカルソート](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/topological_sorting.py)
  - [二部グラフか判定](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/bipartite.py)
  - [根付き木](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/rooted_tree.py)
  - [幅優先探索 (BFS) テンプレート](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/bfs_template.py)
  - [深さ優先探索 (DFS) テンプレート](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/dfs_template.py)
  - [Bellman Ford](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/bellman_ford.py)
  - [Union Find木 (1次元、2次元)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/unionfind.py)
  - [Union Find木 (重み付き)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/weighted_unionfind.py)
  - [ワーシャル・フロイド法](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/warshall_floyd.py)

- 計算量改善のためのテクニック
  - [グリッド上で、ある座標における上下左右の「.」マスの数を数える](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/technique/count_cells.py)
  - [尺取り法 (テンプレート)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/technique/two_pointer_techinique_template.py)
  - [ダブリングのテンプレート](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/technique/doubling_template.py)
  - [2次元累積和](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/technique/cumulative_sum_two_dim.py)
  - [二分探索(bisect)のwrapper](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/technique/bisect_wrapper.py)

- 算数・数学
  - [N進数](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/n_ary_number.py)
  - [拡張ユークリッドの互除法](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/gcd.py)
  - [行列の回転 (右に90度)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/matrix_rotation.py)
  - [組み合わせ](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/combination.py)
  - [桁数](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/digit.py)
  - [最小公倍数](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/lcm.py)
  - [座標圧縮](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/comress.py)
  - [座標の回転・反転操作を行列で計算](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/matrix.py)
  - [三分探索](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/ternary_search.py)
  - [順列 (nPr, mod付き)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/permutation.py)
  - [整数の繰り上げ](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/carry.py)
  - [ソート (キーに条件を指定して比較)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/sort_using_key.py)
  - [素因数分解](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/factorization.py)
  - [素数](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/prime.py)
  - [直積集合を列挙](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/direct_product.py)
  - [パスカルの三角形 (二項係数, nCr)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/pascals_triangle.py)
  - [ビットが1となるインデックスのリストを取得](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/bit_index.py)
  - [約数列挙](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/divisors.py)

- 動的計画法
  - [最長共通部分列 (LCS)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/dp/lcs.py)
  - [最長増加部分列 (LIS)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/dp/lis.py)

- データ構造
  - [BIT (Binary Indexed Tree, Fenwick Tree)、転倒数](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/data_structure/bit.py)
  - [Range Add Query (RAQ) and Range Sum Query (RSQ)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/data_structure/range_add_sum_query.py)
  - [Sorted multiset](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/data_structure/sorted_multi_set.py)
  - [Sorted set](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/data_structure/sorted_set.py)
  - [Trie木](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/data_structure/trie_tree.py)
  - [順序付き集合の代替手段 (C++のsetに相当)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/data_structure/deletable_heapq.py)
  - [セグメント木](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/data_structure/segment_tree.py)
  - [2次元のリストを1次元のリストとして管理](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/data_structure/two_dim_list.py)
  - [配列の最初のi番目の要素までのうち、K番目に大きな値を取得 (i = K, K + 1, ..., n)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/data_structure/kth_greatest_value.py)
  - [配列を昇順/降順に並べたときに、k番目までの要素の総和を高速に計算](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/data_structure/sum_of_top_kth.py)
  - [平衡二分木 (C++のsetに相当)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/data_structure/balancing_tree.py)
  - [ランダムアクセスがO(1)となるdeque](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/data_structure/random_access_deque.py)

- 文字列
  - [アルファベット同士のオフセットを取る](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/string/string.py)
  - [アルファベットにオフセットを加えた値を取得する](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/string/string.py)
  - [タイトルケースに変換](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/string/string.py)
  - [Popcount](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/string/popcount.py)
  - [ランレングス圧縮](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/string/run_length.py)
  - [ローリングハッシュ](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/string/rolling_hash.py)
  - [Z algorithm](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/string/z_algorithm.py)

## 利用環境、開発環境に関する情報

### 利用者、開発者向け

- Python 3.8.0+, 3.9.0+, 3.10.0+, 3.11.0+
- pip

### 開発者向け

- pytest
- GitHub Actions

## 使い方

1. このレポジトリを以下に示す方法でインストールしてください。
2. 使いたいスニペットやアルゴリズムをコピーして、コンテストで提出するコードに貼り付けます。

## インストール

ターミナルで以下のコマンドを貼り付けて、実行してください。

```terminal
$ git clone https://github.com/KATO-Hiro/Somen-Soupy
```

## 参考資料

Readme Driven Development; RDD<sup>[archive.org](http://web.archive.org/web/20220313000343/https://qiita.com/b4b4r07/items/c80d53db9a0fd59086ec)</sup>

[Software licenses for competitive programming library](https://kimiyuki.net/blog/2020/02/14/licenses-for-kyopro-libraries/)

[spaghetti-source/algorithm](https://github.com/spaghetti-source/algorithm)

[Starting with the Python workflow template](https://docs.github.com/en/actions/guides/building-and-testing-python#starting-with-the-python-workflow-template)

## 作者

[@KATO-Hiro](https://twitter.com/k_hiro1818)

## ライセンス

[CC0](https://creativecommons.org/share-your-work/public-domain/cc0)
