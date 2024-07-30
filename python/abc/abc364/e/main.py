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
    N, X, Y = i_map()
    ABN = i_row_list(N)

    '''
    dp[見た料理][食った料理][甘さ] = しょっぱさ
    '''

    dp = [[[10 ** 8] * (X + 1) for _ in range(N + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0

    for r in range(1, N + 1):
        for h in range(r):
            for w in range(1, X + 1):
                if w < ABN[r - 1][0]:
                    dp[r][h][w] = dp[r - 1][h][w]
                    continue
                dp[r][h][w] = min(dp[r][h - 1][w], dp[r][h - 1][w - ABN[r - 1][0]] + ABN[r - 1][1])

    for r in reversed(range(1, N + 1)):
        for w in reversed(range(X)):
            if dp[r][-1][w] <= Y:
                print(r)
                return

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
