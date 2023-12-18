import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
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
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)

sys.setrecursionlimit(10 ** 6)

INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():
    # たぶん累積和だけどやり方覚えてねぇ...
    n = i_input()
    cplist = i_row_list(n)
    q = i_input()
    lrlist = i_row_list(q)
    results = []

    c1_sums = [0] * (n + 1)
    c2_sums = [0] * (n + 1)

    for i, cp in enumerate(cplist):
        if cp[0] == 1:
            c1_sums[i + 1] = c1_sums[i] + cp[1]
            c2_sums[i + 1] = c2_sums[i] + 0
        else:
            c1_sums[i + 1] = c1_sums[i] + 0
            c2_sums[i + 1] = c2_sums[i] + cp[1]

    for lr in lrlist:
        c1r = c1_sums[lr[1]] - c1_sums[lr[0] - 1]
        c2r = c2_sums[lr[1]] - c2_sums[lr[0] - 1]
        results.append([c1r, c2r])

    for result in results:
        print(*result, sep=" ")

if __name__ == '__main__':
    main()
