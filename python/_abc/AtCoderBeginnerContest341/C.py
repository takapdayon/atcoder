import sys, re
from math import ceil, floor, sqrt, pi, gcd, factorial, atan, degrees
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce, cache
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
    H, W, n = i_map()
    t = s_input()
    mas = s_row_list(H)

    result = 0

    for h in range(H):
        for w in range(W):
            can = True
            cur = [h, w]
            if mas[cur[0]][cur[1]] == '#':
                continue
            for st in t:
                if st == 'L':
                    cur[1] -= 1
                if st == 'R':
                    cur[1] += 1
                if st == 'U':
                    cur[0] -= 1
                if st == 'D':
                    cur[0] += 1

                if mas[cur[0]][cur[1]] == '#':
                    can = False
                    break

            if can:
                result += 1

    print(result)

if __name__ == '__main__':
    main()
