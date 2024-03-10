import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial, atan, degrees
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce, cache
from decimal import Decimal, getcontext

# input = sys.stdin.readline
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input() for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [s_list() for _ in range(N)]

sys.setrecursionlimit(10 ** 6)

INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def initial(): return 2 ** 31 - 1

N, Q = i_map()

# 完全二分木のサイズ
size = 1
while size < N:
    size <<= 1

segtree = [initial() for _ in range(size * 2)]
lazy = [INF for _ in range(size * 2)]

def eval(k):
    # 遅延評価実行
    if lazy[k] == INF: return
    if (k < size):
        lazy[k * 2] = lazy[k]
        lazy[k * 2 + 1] = lazy[k]
    segtree[k] = lazy[k]
    lazy[k] = INF

def update(ql, qr, sl, sr, pos, val):
    eval(pos)
    # 完全に含まれている
    if (ql <= sl and sr <= qr):
        lazy[pos] = val
        eval(pos)
    elif (ql < sr and sl < qr):
        sm = (sl + sr) // 2
        update(ql, qr, sl, sm, pos * 2, val)
        update(ql, qr, sm, sr, pos * 2 + 1, val)

def query(ql, qr, sl, sr, pos):
    eval(pos)
    if (qr <= sl or sr <= ql): return INF
    if (ql <= sl and sr <= qr):
        return segtree[pos]
    sm = (sl + sr) // 2
    le = query(ql, qr, sl, sm, pos * 2)
    ri = query(ql, qr, sm, sr, pos * 2 + 1)
    return min(le, ri)

for i in range(Q):
    q = i_list()
    if q[0] == 0:
        update(q[1], q[2] + 1, 0, size, 1, q[3])
    else:
        result = query(q[1], q[1] + 1, 0, size, 1)
        print(result)

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
