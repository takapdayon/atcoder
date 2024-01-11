import sys, re
from math import ceil, floor, sqrt, pi, gcd, factorial, atan, degrees
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
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
def s_row_list(N): return [list(s_map()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)

sys.setrecursionlimit(10 ** 6)

INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():
    n, w = i_map()
    wvrows = i_row_list(n)

    dp = [[0] * (w + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(w + 1):
            # もしオーバーしてしまうなら前回のをそのままスライド
            if w < wvrows[i - 1][0]:
                dp[i][w] = dp[i - 1][w]
                continue

            # 容量が入るなら価値を比較し、より良いほうに変更する
            if dp[i - 1][w] < dp[i - 1][w - wvrows[i - 1][0]] + wvrows[i - 1][1]:
                dp[i][w] = dp[i - 1][w - wvrows[i - 1][0]] + wvrows[i - 1][1]
            else:
                dp[i][w] = dp[i - 1][w]

    print(dp[n][w])

if __name__ == '__main__':
    main()
