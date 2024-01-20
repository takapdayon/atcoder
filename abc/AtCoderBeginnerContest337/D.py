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
def s_row_str(N): return [s_input() for _ in range(N)]
def s_row_str_split(N): return [list(s_input()) for _ in range(N)]
def s_row_list(N): return [list(s_map()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)

sys.setrecursionlimit(10 ** 6)

INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():
    h, w, k = i_map()
    hwrows = s_row_str_split(h)
    w_batu = [0] * (w + 1)
    w_ten = [0] * (w + 1)
    h_batu = [0] * (h + 1)
    h_ten = [0] * (h + 1)

    result = 10 ** 9

    for hi in range(h):
        for wi in range(1, w + 1):
            w_batu[wi] = w_batu[wi - 1] + (hwrows[hi][wi - 1] == 'x' and 1) or 0
            w_ten[wi] = w_ten[wi - 1] + (hwrows[hi][wi - 1] == '.' and 1) or 0

        for i in range(w - k + 1):
            if w_batu[i + k] - w_batu[i]:
                continue
            result = min(result, w_ten[i + k] - w_ten[i])

    for wi in range(w):
        for hi in range(1, h + 1):
            h_batu[hi] = h_batu[hi - 1] + (hwrows[hi - 1][wi] == 'x' and 1) or 0
            h_ten[hi] = h_ten[hi - 1] + (hwrows[hi - 1][wi] == '.' and 1) or 0

        for i in range(h - k + 1):
            if h_batu[i + k] - h_batu[i]:
                continue
            result = min(result, h_ten[i + k] - h_ten[i])

    if result == 10 ** 9:
        print(-1)
    else:
        print(result)

if __name__ == '__main__':
    main()
