import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial, atan, degrees
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
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

def main():
    n, l, r = i_map()
    xlist = i_list()

    '''
    ;メートル以上の制約があるからゴールから貪欲法はできない
    なので、到達地点を含めるか含めないかDPをしていく。この時制約内にあるものに対して配るDPをする
    '''
    dp = [ 10 ** 9 ] * n
    dp[0] = 0
    for i in range(n):
        # 範囲がわからんので、二分探索でlとrの範囲を求める
        pos = xlist[i]
        le = bisect_left(xlist, pos + l)
        ri = bisect_right(xlist, pos + r)
        for ra in range(le, ri):
            dp[ra] = min(dp[i] + 1, dp[ra])

    print(dp[n - 1])

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
