# Python Seminar 2023

本ページは 2023 年に [Team SNAC Tsukuba](https://www.math.tsukuba.ac.jp/~snac/) で実施する Python Seminar 2023 の内容をまとめたものである．
このセミナーでは，プログラミング言語 Python のインストールと基本的な使いかたを学び，その応用として数式処理ライブラリ SymPy に触れる．

## Pythonの基本

[Python Boot Camp のテキスト](https://pycamp.pycon.jp/textbook/index.html)を使う．
[Python Boot Camp](https://pycamp-lp.pycon.jp) は全国に Python を広めることを目的とし，チュートリアル講座を実施するイベント[^1]．

[^1]:2018 年には筑波大学を会場として [Python Boot Camp in 茨城](https://pyconjp.blogspot.com/2018/08/pycamp-in-ibaraki-report.html)も開催されている．
筆者はここで初めて Python に触れた．

テキストは以下の部分を用いる[^2]．

[^2]:今回は数学との関連が薄いので扱わなかったが，省略した部分も面白いので，ぜひ読んでみてほしい．
5.1 のファイル操作ができるだけで，かなり実用的なプログラムを作れるようになる．
第 7 章ではスクレイピングの演習を通して， Python の既存のライブラリがとても強力であることがわかる．

- 第 4 章までの全て．
- 第 5 章は主に 5.2 のみ扱う．ライブラリの理解のために，5.3 の代わりに Python 標準ライブラリの 1 つである `math` モジュールを扱う．
- 第 6 章は全て．
- 第 7 章はウェブサイトのスクレイピングに関する演習なので，扱わない.

テキストに沿って学習を進め，第 4 章まで進んだら以下の演習問題を解く．

### 演習：ユークリッドの互除法

ユークリッドの互除法を用いて，整数 $a, b$ の最大公約数を求めるプログラムを作成せよ．

- [解答例](gcd.py)

### 演習：エラトステネスの篩

[エラトステネスの篩](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%A9%E3%83%88%E3%82%B9%E3%83%86%E3%83%8D%E3%82%B9%E3%81%AE%E7%AF%A9)を用いて，
$n$ 以下の全ての素数を求めるプログラムを作成せよ．

- [解答例1](eratosthenes1.py)
- [解答例2](eratosthenes2.py)（[参考文献](https://qiita.com/ytaki0801/items/cc58da6eafd3ec4d91ba)）

### `math` モジュール

Python の標準ライブラリの 1 つで数学関連の関数を提供している．
例えば 3 の正の平方根は以下のように求めることができる．

```python
>>> import math
>>> x = math.sqrt(3)
>>> x
1.7320508075688772
```

返り値は浮動小数点数であるため，厳密に $\sqrt{3}$ とは一致しない．
ある誤差を許容して値が近いことを調べるためには，`math.isclose(a, b)` を用いる．

```python
>>> x**2 == 3
False
>>> math.iscolose(x**2, 3)
True
```

このような誤差を許容せず，厳密に $\sqrt{3}$ などの代数的数を扱うことができる方法として，数式処理ライブラリの SymPy を紹介する．

## SymPy

[SymPy](https://sympy.org) は Python の数式処理ライブラリ．[公式のチュートリアル](https://docs.sympy.org/latest/tutorials)

### 演習：PRSの計算時間[^3]

[^3]:[参考文献：横山和弘．多項式と計算機代数．朝倉書店．2022](https://www.asakura.co.jp/detail.php?book_code=11767)

整数係数の多項式 $f,g$ に対して，ユークリッドの互除法による PRS，原始的 PRS，部分終結式 PRS をそれぞれ求めるプログラムを作成せよ．
またそれぞれの PRS の計算にかかった時間を実際に計測せよ．

PRS の計算には以下を用いることが出来る．

- `dup_euclidean_prs(f, g)`
  - 多項式 $f,g$ に対して，ユークリッドの互助法による PRS をリストで返す．
  - [ソースコード](https://github.com/sympy/sympy/blob/d2be7bacd2604e98a642f74028e8f0d7d6084f78/sympy/polys/euclidtools.py#L194-L231)
- `dup_primitive_prs(f, g)`
  - 多項式 $f,g$ に対して，原始的 PRS をリストで返す．
  - [ソースコード](https://github.com/sympy/sympy/blob/d2be7bacd2604e98a642f74028e8f0d7d6084f78/sympy/polys/euclidtools.py#L251-L288)
- `dup_prs_resultant(f, g)`
  - 多項式 $f,g$ に対して，第1要素が終結式，第2要素が PRS のリストであるようなタプルを返す．すなわち `dup_prs_resultant(f, g)[1]` で部分終結式 PRS を返す．
  - [ソースコード](https://github.com/sympy/sympy/blob/d2be7bacd2604e98a642f74028e8f0d7d6084f78/sympy/polys/euclidtools.py#L405-L427)

また，Python のプログラムの計算処理時間を計測するには `time.perf_counter` を用いると良い．（[参考文献](https://qiita.com/Nananananamber/items/b9e22d7011404151ca07)）

```python
import time
start = time.perf_counter
# 処理
end = time.perf_counter
print(end - start)
# 処理時間出力
```

- [解答例](prs-time.py)

### 演習：擬除算 PRS アルゴリズム

原始的 PRS を計算する関数 `dup_primitive_prs(f, g)` の
[ソースコード](https://github.com/sympy/sympy/blob/d2be7bacd2604e98a642f74028e8f0d7d6084f78/sympy/polys/euclidtools.py#L251-L288)を参考に，
多項式 $f, g$ に対して，擬除算 PRS を計算する関数 `prem_prs` を作成せよ．
また，上の演習で作成した PRS の計算処理時間を計測するプログラムに，擬除算 PRS も加えよ．

- [解答例](prs-time2.py)

## その他の数学に関連する Python ライブラリやソフトウェア

- [NumPy](https://numpy.org/)
  - 行列などの多次元配列や，それに関連した関数を扱うライブラリ．
- [SciPy](https://scipy.org/)
  - 数値解析のためのライブラリ．NumPy を基礎にしている．
- [Matplotlib](https://matplotlib.org/)
  - グラフを描画するためのライブラリ．
- [pandas](https://pandas.pydata.org/)
  - 表のような形をしたデータの操作や解析のためのライブラリ．
- [SageMath](https://www.sagemath.org/)
  - 数学の幅広い処理を Python で使えるソフトウェア．
