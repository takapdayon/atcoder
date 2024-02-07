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
    n, q = i_map()
    s = s_input()
    rs = s[::-1]
    h = [0] * (n + 1)
    rh = [0] * (n + 1)

    for i in range(n):
        h[i + 1] = (h[i] * 100 + ord(s[i])) % MOD
        rh[i + 1] = (rh[i] * 100 + ord(rs[i])) % MOD

    for i in range(q):
        l, r = i_map()
        rl, rr = (n - r + 1), (n - l + 1)
        h_v = h[r] - (h[l - 1] * pow(100, r - l + 1, MOD)) % MOD
        if h_v < 0:
            h_v += MOD
        rh_v = rh[rr] - (rh[rl - 1] * pow(100, rr - rl + 1, MOD)) % MOD
        if rh_v < 0:
            rh_v += MOD
        if h_v == rh_v:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
