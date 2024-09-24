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
    N = int(input())
    ABCDN = [map(int, input().split()) for _ in range(N)]

    MAX_GRID = 1500
    grid = [[0] * (MAX_GRID + 1) for _ in range(MAX_GRID + 1)]

    for a, b, c, d in ABCDN:
        grid[a][b] += 1
        grid[a][d] -= 1
        grid[c][b] -= 1
        grid[c][d] += 1

    for h in range(MAX_GRID + 1):
        for w in range(1, MAX_GRID + 1):
            grid[h][w] += grid[h][w - 1]

    for h in range(1, MAX_GRID + 1):
        for w in range(MAX_GRID + 1):
            grid[h][w] += grid[h - 1][w]

    result = 0

    for h in range(MAX_GRID + 1):
        for w in range(MAX_GRID + 1):
            if grid[h][w]:
                result += 1
    print(result)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
