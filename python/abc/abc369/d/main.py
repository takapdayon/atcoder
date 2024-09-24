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
    AN = i_list()

    dp = [[0, 0, 0, 0] for _ in range(N + 1)]
    '''
    奇数で逃がす
    偶数で逃がす
    奇数で倒す
    偶数で倒す
    上記でDP
    '''
    for i in range(1, N + 1):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][3])
        dp[i][2] = max(dp[i - 1][1] + AN[i - 1], dp[i - 1][3] + AN[i - 1])
        if i == 1:
            dp[i][3] = dp[i - 1][3]
        else:
            dp[i][3] = max(dp[i - 1][0] + AN[i - 1] * 2, dp[i - 1][2] + AN[i - 1] * 2)

    print(max(dp[-1]))

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
