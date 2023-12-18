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
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)

sys.setrecursionlimit(10 ** 6)

INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []


def recursive(count, n, l):
    tmp = 0
    if count + 1 == n:
        tmp += 1
    if count + l == n:
        tmp += 1

    if count >= n:
        return tmp

    return tmp + recursive(count + 1, n, l) + recursive(count + l, n, l)

def main():
    n, l = i_map()

    dp = [[0, 0] for _ in range(n + 1)]

    dp[0][0] = 1
    if (n >= l):
        dp[l][1] = 1

    for i in range(1, n + 1):
        dp[i][0] += dp[i - 1][0]
        if i + l <= n:
            dp[i + l][0] += dp[i][0]

        if l > i:
            continue
        dp[i][1] += dp[i - 1][1]
        if i + l <= n:
            dp[i + l][1] += dp[i][1]

    print(sum(dp[-1]) % MOD)

if __name__ == '__main__':
    main()
