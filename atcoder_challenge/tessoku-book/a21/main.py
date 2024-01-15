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
    n = i_input()
    parows = i_row_list(n)
    parows.append([0, 0])

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    max_value = 0

    for i in range(1, n + 1):
        for w in reversed(range(i - 1, n)):
            if i == 1:
                from_i = dp[i - 1][w]
                from_w = dp[i][w + 1] + (i <= parows[w + 1][0] <= w + 1 and parows[w + 1][1]) or 0
            else:
                from_i = dp[i - 1][w] + (i <= parows[i - 2][0] <= w + 1 and parows[i - 2][1]) or 0
                from_w = dp[i][w + 1] + (i <= parows[w + 1][0] <= w + 1 and parows[w + 1][1]) or 0

            dp[i][w] = max(from_i, from_w)
            max_value = max(max_value, dp[i][w])

    print(max_value)

if __name__ == '__main__':
    main()
