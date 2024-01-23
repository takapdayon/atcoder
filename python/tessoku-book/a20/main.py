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
    s = s_input()
    t = s_input()
    s_len = len(s)
    t_len = len(t)

    dp = [[0] * (s_len + 1) for _ in range(t_len + 1)]

    for i in range(t_len + 1):
        for w in range(s_len + 1):
            if i >= 1 and w >= 1:
                dp[i][w] = max(dp[i - 1][w], dp[i][w - 1], (s[w - 1] == t[i - 1] and dp[i - 1][w - 1] + 1) or 0)
                continue

            if i >= 1:
                dp[i][w] = dp[i - 1][w]
                continue
            else:
                dp[i][w] = dp[i][w - 1]

    print(dp[t_len][s_len])

if __name__ == '__main__':
    main()
