import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial, atan, degrees
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce, cache
from decimal import Decimal, getcontext
from sortedcontainers import SortedSet, SortedList, SortedDict

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
def s_row_list(N): return [list(s_input()) for _ in range(N)]

sys.setrecursionlimit(10 ** 6)

INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

N, Q = i_map()
alist = i_list()

def initial():
    # 左の1の数, 右の1の数, 右の1の数, 左の0の数
    return (0, 0, 0, 0)

size = 1
# 完全二分木
while size < N:
    size <<= 1

segtree = [initial() for _ in range(size * 2)]
lazy = [initial() for _ in range(size * 2)]

def eval(pos):
    if lazy[pos] == initial():
        return initial()

    # 子を持てる場合は下に伝える
    if (pos < size):
        lazy[pos * 2] = lazy[pos]
        lazy[pos * 2 + 1] = lazy[pos]
    segtree[pos] = lazy[pos]
    lazy[pos] = initial()

def op(x, y):
    x1, x2, x3, x4 = x
    y1, y2, y3, y4 = y
    a1, a2, a3, a4 = x1 + y1 + (x3 * y4), x2 + y2, x3 + y3, a4 + y4
    return (a1, a2, a3, a4)

def update(ql, qr, sl, sr, pos, val):
    eval(pos)

    # 完全に含まれてない
    if (qr <= sl or sr <= ql):
        return initial()

    # 完全に含まれている
    if (ql <= sl and sr <= qr):
        lazy[pos] = val
        eval(pos)

    # 部分
    sm = (sl + sr) // 2
    le = update(ql, qr, sl, sm, pos * 2, val)
    ri = update(ql, qr, sm, sr, pos * 2 + 1, val)
    segtree[pos] = op(le, ri)
    return segtree[pos]

def query(ql, qr, sl, sr, pos):
    eval(pos)
    # 完全に含まれてない
    if (qr <= sl or sr <= ql):
        return initial()

    # 完全に含まれている
    if (ql <= sl and sr <= qr):
        return segtree[pos]

    # 部分
    sm = (sl + sr) // 2
    le = query(ql, qr, sl, sm, pos * 2)
    ri = query(ql, qr, sm, sr, pos * 2 + 1)
    return op(le, ri)

'''
# 左の1の数, 右の0の数, 右の1の数, 左の0の数
1, 1, 0, 1の時
11側
(2, 0, 2, 0)
01側
(0, 0, 1, 1)
(2, 1, 1, 1)

0, 0, 1, 0になる

ノードAの時点での
左の1の数、右の0の数 =
'''

for i, a in enumerate(alist):
    if a == 0:
        # 左の1の数, 右の0の数, 右の1の数, 左の0の数
        update(i, i + 1, 0, size, 1, (0, 1, 0, 1))
    else:
        update(i, i + 1, 0, size, 1, (1, 0, 1, 0))

for i in range(Q):
    t, l, r = i_map()
    '''
    ほしいもの:
    右の0の数
    左の1の数
    '''
    if t == 1:
        update(l - 1, r, 0, size, 1)
    else:
        result = query(l - 1, r, 0, size)
        print(result[0] * result[2])

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
