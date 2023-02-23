import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd, prod
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
from functools import lru_cache

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
    slist = i_row(n)
    d = deque()
    culc = 1
    max_len = 0

    if 0 in slist:
        print(n)
        return

    if k == 0:
        print(0)
        return

    for i in slist:
        culc *= i
        d.append(i)
        if culc <= k:
            max_len = max(max_len, len(d))
            continue
        while culc > k:
            left = d.popleft()
            culc /= left

    print(max_len)

if __name__ == '__main__':
    main()
