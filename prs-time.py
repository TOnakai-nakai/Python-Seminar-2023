from sympy import *
import time

result = []

R, x = ring('x', QQ)
f = x**6 + x**4 + 1
g = 3*x**4 + 5*x**3 - 7*x**2 + 1

# ユークリッドの互除法によるPRSの計算時間
start = time.perf_counter()
euclidean_prs = R.dup_euclidean_prs(f, g)
end = time.perf_counter()
result.append({'prs': euclidean_prs, 'time': end - start})

R, x = ring('x', ZZ)
f = x**6 + x**4 + 1
g = 3*x**4 + 5*x**3 - 7*x**2 + 1

# 原始的PRSの計算時間
start = time.perf_counter()
primitive_prs = R.dup_primitive_prs(f, g)
end = time.perf_counter()
result.append({'prs': primitive_prs, 'time': end - start})

# 部分終結式PRSの計算時間
start = time.perf_counter()
resultant_prs = R.dup_prs_resultant(f, g)[1]
end = time.perf_counter()
result.append({'prs': resultant_prs, 'time': end - start})

prs_name = ['ユークリッドの互除法によるPRS', '原始的PRS', '部分終結式PRS']

for i in range(len(result)):
    print('=================================================')
    print(prs_name[i])
    print('実行時間 :', result[i].get('time'))
    print('-------------------------------------------------')
    for j in range(len(result[i].get('prs'))):
        print(result[i].get('prs')[j])