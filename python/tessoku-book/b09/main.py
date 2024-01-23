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
    abcdlist = i_row_list(n)
    length = 1501

    counter_w = [[0] * (length + 1) for _ in range(length + 1)]
    counter = [[0] * (length + 1) for _ in range(length + 1)]

    for a, b, c, d in abcdlist:
        counter_w[a][b] += 1
        counter_w[a][d] -= 1
        counter_w[c][b] -= 1
        counter_w[c][d] += 1

    for hi in range(1, length + 1):
        for wi in range(1, length + 1):
            counter_w[hi][wi] = counter_w[hi][wi - 1] + counter_w[hi][wi]

    for hi in range(1, length + 1):
        for wi in range(1, length + 1):
            counter[hi][wi] = counter[hi - 1][wi] + counter_w[hi][wi]

    result = 0

    for hi in range(1, length + 1):
        for wi in range(1, length + 1):
            if counter[hi][wi]:
                result += 1

    print(result)

if __name__ == '__main__':
    main()
