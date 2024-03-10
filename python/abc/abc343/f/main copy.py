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
def s_row_list(N): return [s_list() for _ in range(N)]

sys.setrecursionlimit(10 ** 6)

INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def op(node1, node2):
    # 1 < Aなため、node内でかぶりは絶対にない
    n1a, n1ac, n1b, n1bc = node1
    n2a, n2ac, n2b, n2bc = node2

    if n1a == n2a:
        n1ac += n2ac
        if n1b == n2b:
            n1bc += n2bc
        elif n1b < n2b:
            n1b, n1bc = n2b, n2bc
    elif n1a < n2a:
        tmp, tmpc = n1a, n1ac
        n1a, n1ac = n2a, n2ac
        if tmp == n2b:
            n1b = tmp
            n1bc = tmpc
            n1bc += n2bc
        elif tmp < n2b:
            n1b, n1bc = n2b, n2bc
        else:
            n1b, n1bc = tmp, tmpc
    else:
        if n1b == n2a:
            n1bc += n2ac
        elif n1b < n2a:
            n1b, n1bc = n2a, n2ac

    return (n1a, n1ac, n1b, n1bc)

def initial():
    return (0, 0, -1, 0)

def update(segtree, size, p, x):
    pos = size + p
    segtree[pos] = x
    while True:
        pos //= 2
        if pos == 0:
            break
        segtree[pos] = op(segtree[pos * 2], segtree[pos * 2 + 1])

def query(segtree, ql, qr, sl, sr, pos):
    # 完全に含まれてない
    if (sr <= ql or qr <= sl):
        return initial()

    # 完全に含まれている
    if (ql <= sl and sr <= qr):
        return segtree[pos]

    # 部分
    sm = (sl + sr) // 2
    le = query(segtree, ql, qr, sl, sm, pos * 2)
    ri = query(segtree, ql, qr, sm, sr, pos * 2 + 1)
    return op(le, ri)

def main():
    N, Q = i_map()
    alist = i_list()

    # 完全二分木サイズ
    size = 1
    while size < N:
        size <<= 1

    segtree = [initial() for _ in range(size * 2)]

    for i, a in enumerate(alist):
        update(segtree, size, i, (a, 1, 0, 0))

    for q in range(Q):
        com, x, y = i_map()
        if com == 1:
            update(segtree, size, x - 1, (y, 1, 0, 0))
        else:
            result = query(segtree, x - 1, y, 0, size, 1)
            print(result[3])

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
