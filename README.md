# Python Seminar 2023

本ページは2023年に[Team SNSC Tsukuba](https://www.math.tsukuba.ac.jp/~snac/)で実施するPython Seminar 2023の内容をまとめたものである．このセミナーでは，プログラミング言語Pythonのインストールと基本的な使いかたを学び，その応用として数式処理ライブラリSymPyに触れる．

## Pythonの基本

[Python Boot Camp](https://pycamp-lp.pycon.jp)の[テキスト](https://pycamp.pycon.jp/textbook/index.html)を使う．Python Boot Campは全国にPythonを広めることを目的とし，チュートリアル講座を実施するイベント．2018年には筑波大学を会場として[Python Boot Camp in 茨城](https://pyconjp.blogspot.com/2018/08/pycamp-in-ibaraki-report.html)も開催されている．

テキストは以下の部分を用いる．

- 第4章までの全て．
- 第5章は主に5.2のみ扱う．ライブラリの理解のために，5.3には少し触れる．
- 第6章は全て．
- 第7章はウェブサイトのスクレイピングに関する演習なので，扱わない.

### 演習：エラトステネスの篩

第4章まで学習したら，[エラトステネスの篩](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%A9%E3%83%88%E3%82%B9%E3%83%86%E3%83%8D%E3%82%B9%E3%81%AE%E7%AF%A9)を用いて， $n$ 以下の全ての素数を求めるプログラムを作成せよ．

- [解答例1](eratosthenes1.py)
- [解答例2](eratosthenes2.py)（[参考文献](https://qiita.com/ytaki0801/items/cc58da6eafd3ec4d91ba)）

## SymPy

[SymPy](https://sympy.org)はPythonの数式処理ライブラリ．[公式のチュートリアル](https://docs.sympy.org/latest/tutorials)

### 演習：PRSの計算時間

整数係数の多項式 $f,g$ に対して，ユークリッドの互除法によるPRS，原始的PRS，部分終結式PRSをそれぞれ求めるプログラムを作成せよ．またそれぞれのPRSの計算にかかった時間を実際に計測せよ．

PRSの計算には以下を用いることが出来る．

- `dup_euclidean_prs(f, g)`
  - 多項式 $f,g$ に対して，ユークリッドの互助法によるPRSをリストで返す．[ドキュメント]
- `dup_primitive_prs(f, g)`
  - 多項式 $f,g$ に対して，原始的PRSをリストで返す．[ドキュメント]
- `dup_prs_resultant(f, g)`
  - 多項式 $f,g$ に対して，第1要素が終結式，第2要素がPRSのリストであるようなタプルを返す．すなわち `dup_prs_resultant(f, g)[1]` で部分終結式PRSを返す．

また，Pythonのプログラムの計算処理時間を計測するには `time.perf_counter` を用いると良い．（[参考文献](https://qiita.com/Nananananamber/items/b9e22d7011404151ca07)）

```python
import time
start = time.perf_counter
# 処理
end = time.perf_counter
print(end - start)
# 処理時間出力
```

- [解答例](prs-time.py)
