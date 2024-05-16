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
    S = s_row_list(H)
    uf = DSU(H * W)
    result = set()

    for h in range(H):
        for w in range(W):
            if S[h][w] == '.':
                continue
            for nhi, nwi in zip([1, 1, 0, -1, -1, -1, 0, 1], [0, -1, -1, -1, 0, 1, 1, 1]):
                nh, nw = h + nhi, w + nwi
                if nh < 0 or nh >= H:
                    continue
                if nw < 0 or nw >= W:
                    continue
                if S[nh][nw] == '.':
                    continue
                uf.merge(h * W + w , nh * W + nw)

    for h in range(H):
        for w in range(W):
            if S[h][w] == '.':
                continue
            result.add(uf.leader(h * W + w))

    print(len(result))

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
