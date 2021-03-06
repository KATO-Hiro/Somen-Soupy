# Somen-Soupy

![build](https://github.com/KATO-Hiro/Somen-Soupy/workflows/Python%20package/badge.svg)

## 説明

- 競技プログラミングのコンテストで使用するスニペットやアルゴリズムがPython3で実装されています。

## 主な機能

- グラフ理論
  - [ダイクストラ法](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/dijkstra.py)
  - [根付き木](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/rooted_tree.py)
  - [Union Find木](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/unionfind.py)
  - [Union Find木 (重み付き)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/weighted_unionfind.py)
  - [ワーシャル・フロイド法](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/graph/warshall_floyd.py)

- 算数・数学
  - [N進数](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/n_ary_number.py)
  - [拡張ユークリッドの互除法](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/gcd.py)
  - [組み合わせ](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/combination.py)
  - [桁数](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/digit.py)
  - [最小公倍数](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/lcm.py)
  - [座標圧縮](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/comress.py)
  - [素因数分解](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/factorization.py)
  - [素数](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/math/prime.py)

- 動的計画法
  - [最長共通部分列 (LCS)](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/dp/lcs.py)

- 文字列
  - [タイトルケースに変換](https://github.com/KATO-Hiro/Somen-Soupy/blob/master/snippets/string/string.py)

## 利用環境、開発環境に関する情報

### 利用者、開発者向け

- Python 3.6.0+, 3.7.0+, 3.8.0+, 3.9.0+
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

[Readme Driven Development; RDD](https://qiita.com/b4b4r07/items/c80d53db9a0fd59086ec)

[Software licenses for competitive programming library](https://kimiyuki.net/blog/2020/02/14/licenses-for-kyopro-libraries/)

[spaghetti-source/algorithm](https://github.com/spaghetti-source/algorithm)

[Starting with the Python workflow template](https://docs.github.com/en/actions/guides/building-and-testing-python#starting-with-the-python-workflow-template)

## 作者

[@KATO-Hiro](https://twitter.com/k_hiro1818)

## ライセンス

[CC0](https://creativecommons.org/share-your-work/public-domain/cc0)
