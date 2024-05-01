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
    N = i_input()
    papers = i_row_list(N)
    ML = 1000
    grid = [[0] * (ML + 2) for _ in range(ML + 2)]

    for lw, lh, rw, rh in papers:
        grid[lh][lw] += 1
        grid[lh][rw] -= 1
        grid[rh][lw] -= 1
        grid[rh][rw] += 1

    # 二次元累積和
    for hi in range(ML + 1):
        for wi in range(1, ML + 1):
            grid[hi][wi] = grid[hi][wi] + grid[hi][wi - 1]

    for hi in range(1, ML + 1):
        for wi in range(ML + 1):
            grid[hi][wi] = grid[hi][wi] + grid[hi - 1][wi]

    ans = [0] * (N + 1)
    for h in range(ML + 1):
        for w in range(ML + 1):
            ans[grid[h][w]] += 1

    for a in ans[1:]:
        print(a)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
