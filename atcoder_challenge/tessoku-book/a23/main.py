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
    n, m = i_map()
    bit = 2 ** n
    arows = i_row_list(m)
    dp = [ [ 10 ** 2 ] * bit for _ in range(m + 1)]
    dp[0][0] = 0

    for i in range(1, m + 1):
        for w in range(bit):
            already = [ 1 ] * n
            for k in range(n):
                if (w // (2 ** k)) % 2 == 0:
                    already[k] = 0
            v = 0
            for k in range(n):
                if already[k] == 1 or arows[i - 1][k] == 1:
                    v += (2 ** k)

            dp[i][w] = min(dp[i][w], dp[i - 1][w])
            dp[i][v] = min(dp[i][v], dp[i - 1][w] + 1)

    if dp[m][bit - 1] == 10 ** 9:
        print(-1)
    else:
        print(dp[m][bit - 1])

if __name__ == '__main__':
    main()
