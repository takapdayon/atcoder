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

def initial(): return 0

def op(): return sum

def update(segtree, size, p, x):
    pos = p + size
    segtree[pos] += x
    while True:
        pos //= 2
        if pos == 0:
            break
        segtree[pos] = op()([segtree[pos * 2], segtree[pos * 2 + 1]])

def query(segtree, ql, qr, sl, sr, pos):
    # 完全含まれん
    if (sr <= ql or qr <= sl):
        return initial()

    # 完全に含まれる
    if (ql <= sl and sr <= qr):
        return segtree[pos]

    # 部分的
    sm = (sl + sr) // 2
    le = query(segtree, ql, qr, sl, sm, pos * 2)
    ri = query(segtree, ql, qr, sm, sr, pos * 2 + 1)
    return op()([le, ri])

def main():
    N, Q = i_map()
    size = 1

    # 完全二分木作成サイズ
    while size < N:
        size <<= 1

    segtree = [initial() for _ in range(size * 2)]

    for q in range(Q):
        com, x, y = i_map()
        if com == 0:
            update(segtree, size, x - 1, y)
        else:
            result = query(segtree, x - 1, y, 0, size, 1)
            print(result)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
