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

from atcoder.dsu import DSU

def main():
    H, W = i_map()
    Q = i_input()
    grid = [[False] * (W + 1) for _ in range(H + 1)]
    uf = DSU(H * W + 1)

    for q in range(Q):
        query = i_list()
        if query[0] == 1:
            grid[query[1]][query[2]] = True
            for h, w in zip([1, 0, -1, 0], [0, -1, 0, 1]):
                nh, nw = query[1] + h, query[2] + w
                if nh > H or nh < 1:
                    continue
                if nw > W or nw < 1:
                    continue
                if grid[nh][nw]:
                    uf.merge((query[1] - 1) * W + query[2], (nh - 1) * W + nw)

        else:
            ra, ca, rb, cb = query[1], query[2], query[3], query[4]
            if grid[ra][ca] and grid[rb][cb]:
                print(uf.same((ra - 1) * W + ca, (rb - 1) * W + cb) and 'Yes' or 'No')
            else:
                print('No')

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
