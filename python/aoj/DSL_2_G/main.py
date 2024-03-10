import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial, atan, degrees
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce, cache
from decimal import Decimal, getcontext

from colorama import init

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

def initial():
    return 0

N, Q = i_map()

# 完全二分木を作る
size = 1
while size < N:
    size <<= 1

segtree = [initial() for _ in range(size * 2)]
lazy = [initial() for _ in range(size * 2)]

def op(x, y):
    return x + y

def eval(pos):
    if lazy[pos] == initial():
        return initial()

    if (pos < size):
        lazy[pos * 2] += lazy[pos]
        lazy[pos * 2 + 1] += lazy[pos]

    segtree[pos] = lazy[pos]
    lazy[pos] = initial()

def update(ql, qr, sl, sr, pos, val):
    eval(pos)
    if (qr <= sl or sr <= ql):
        return initial()
    if (ql <= sl and sr <= qr):
        lazy[pos] += val
        eval(pos)
        return segtree[pos]

    sm = (sl + sr) // 2
    le = update(ql, qr, sl, sm, pos * 2, val)
    ri = update(ql, qr, sm, sr, pos * 2 + 1, val)
    segtree[pos] = op(le, ri)
    return segtree[pos]

def query(ql, qr, sl, sr, pos):
    eval(pos)
    if (qr <= sl or sr <= ql):
        return initial()
    if (ql <= sl or sr <= qr):
        return segtree[pos]
    sm = (sl + sr) // 2
    le = query(ql, qr, sl, sm, pos * 2)
    ri = query(ql, qr, sm, sr, pos * 2 + 1)
    return op(le, ri)

for i in range(Q):
    q = i_list()
    if q[0] == 0:
        update(q[1] - 1, q[2], 0, size, 1, q[3])
    else:
        result = query(q[1] - 1, q[2], 0, size, 1)
        print(result)

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
