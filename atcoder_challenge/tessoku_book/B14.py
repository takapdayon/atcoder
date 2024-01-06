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

def main():
    n, k = i_map()
    alist = i_list()
    fhalf_alist = []
    lhalf_alist = []

    combination = {}
    result = 0

    for i in range(1, len(alist[::2]) + 1):
        for comb in combinations(alist[::2], i):
            fhalf_alist.append(sum(comb))

    for i in range(1, len(alist[1::2]) + 1):
        for comb in combinations(alist[1::2], i):
            lhalf_alist.append(sum(comb))

    for fhalf_a in fhalf_alist:
        combination[fhalf_a] = 1

    lhalf_alist.append(0)

    for lhalf_a in (lhalf_alist):
        result += combination.get(k - lhalf_a, 0)

    print((result and 'Yes') or 'No')


if __name__ == '__main__':
    main()
