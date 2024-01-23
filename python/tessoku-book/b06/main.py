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
    alist = i_list()
    q = i_input()
    lrlist = i_row_list(q)
    prefix_sum_atari = [0] * (n + 1)
    prefix_sum_hazure = [0] * (n + 1)

    for i, a in enumerate(alist, 1):
        prefix_sum_atari[i] = prefix_sum_atari[i - 1] + a
        prefix_sum_hazure[i] = prefix_sum_hazure[i - 1] + (a == 0 and 1) or 0

    for l, r in lrlist:
        atari_count = prefix_sum_atari[r] - prefix_sum_atari[l - 1]
        hazure_count = prefix_sum_hazure[r] - prefix_sum_hazure[l - 1]

        if atari_count > hazure_count:
            print('win')
        elif atari_count < hazure_count:
            print('lose')
        else:
            print('draw')

if __name__ == '__main__':
    main()
