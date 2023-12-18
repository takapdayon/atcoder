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
    h, w = i_map()
    arows = i_row_list(h)
    brows = i_row_list(h)

    result = 0

    for h_i in range(h - 1):
        for w_i in range(w - 1):
            diff = brows[h_i][w_i] - arows[h_i][w_i]
            if diff == 0:
                continue
            result += abs(diff)
            arows[h_i][w_i] += diff
            arows[h_i + 1][w_i] += diff
            arows[h_i][w_i + 1] += diff
            arows[h_i + 1][w_i + 1] += diff

    if arows != brows:
        print("No")
        return

    print("Yes")
    print(result)

if __name__ == '__main__':
    main()
