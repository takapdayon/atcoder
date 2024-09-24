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

def main():
    H, W, Q = i_map()
    RCQ = i_row_list(Q)
    count = H * W
    grid = [[False] * (W + 1) for _ in range(H + 1)]
    h_uf = [SortedSet(i for i in range(1, H + 1)) for _ in range(W + 1)]
    w_uf = [SortedSet(i for i in range(1, W + 1)) for _ in range(H + 1)]

    for r, c in RCQ:
        if not grid[r][c]:
            count -= 1
            grid[r][c] = True
            h_uf[c].discard(r)
            w_uf[r].discard(c)
            continue

        # 上下左右に壊せる壁があるか見たい
        h_index = h_uf[c].bisect_left(r)
        if h_index != 0:
            value = h_uf[c][h_index - 1]
            grid[value][c] = True
            h_uf[c].discard(value)
            w_uf[value].discard(c)
            h_index -= 1
            count -= 1
        if len(h_uf[c]) and h_index != len(h_uf[c]):
            value = h_uf[c][h_index]
            grid[value][c] = True
            h_uf[c].discard(value)
            w_uf[value].discard(c)
            count -= 1

        w_index = w_uf[r].bisect_left(c)
        if w_index != 0:
            value = w_uf[r][w_index - 1]
            grid[r][value] = True
            w_uf[r].discard(value)
            h_uf[value].discard(r)
            w_index -= 1
            count -= 1
        if len(w_uf[r]) and w_index != len(w_uf[r]):
            value = w_uf[r][w_index]
            grid[r][value] = True
            w_uf[r].discard(value)
            h_uf[value].discard(r)
            count -= 1

    print(count)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
