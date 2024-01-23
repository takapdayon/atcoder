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
    d = i_input()
    n = i_input()
    lrlist = i_row_list(n)

    count_start = [0] * (d + 1)
    count_end = [0] * (d + 1)
    prefix_sum_start = [0] * (d + 1)
    prefix_sum_end = [0] * (d + 1)

    for l, r in lrlist:
        count_start[l] += 1
        count_end[r] += 1

    for i, (cs, ce) in enumerate(zip(count_start, count_end)):
        prefix_sum_start[i] = prefix_sum_start[i - 1] + cs
        prefix_sum_end[i] = prefix_sum_end[i - 1] + ce

    for i in range(1, d + 1):
        print(prefix_sum_start[i] - prefix_sum_end[i - 1])

if __name__ == '__main__':
    main()
