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
    h, w, n = i_map()
    mas = [[True] * w for _ in range(h)]
    to = 1
    loc = [0, 0]

    for i in range(n):
        mas[loc[0]][loc[1]] = not mas[loc[0]][loc[1]]
        if not mas[loc[0]][loc[1]]:
            if to == 1:
                loc[1] = loc[1] + 1 if loc[1] + 1 != w else 0
            if to == 2:
                loc[0] = loc[0] + 1 if loc[0] + 1 != h else 0
            if to == 3:
                loc[1] = loc[1] - 1 if loc[1] -1 != -1 else w - 1
            if to == 4:
                loc[0] = loc[0] - 1 if loc[0] - 1 != -1 else h - 1
            to = to + 1 if to != 4 else 1
        else:
            if to == 1:
                loc[1] = loc[1] - 1 if loc[1] - 1 != -1 else w - 1
            if to == 2:
                loc[0] = loc[0] - 1 if loc[0] - 1 != -1 else h - 1
            if to == 3:
                loc[1] = loc[1] + 1 if loc[1] + 1 != w else 0
            if to == 4:
                loc[0] = loc[0] + 1 if loc[0] + 1 != h else 0
            to = to - 1 if to != 1 else 4

    for m in mas:
        print(''.join('.' if i else '#' for i in m))

if __name__ == '__main__':
    main()

