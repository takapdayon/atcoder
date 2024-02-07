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

def update(segtree, n, x):
    pos = x + n - 1
    segtree[pos] = 1
    while True:
        pos //= 2
        if pos == 0:
            break
        segtree[pos] = segtree[pos * 2] + segtree[pos * 2 + 1]

def count(segtree, n, x):
    le = x + n
    ri = n * 2
    count = 0
    while le < ri:
        if le % 2 == 1:
            count += segtree[le]
            le += 1
        le //= 2
        if ri % 2 == 1:
            count += segtree[ri - 1]
            ri -= 1
        ri //= 2
    return count

def main():
    n = i_input()
    alist = i_list()
    segtree = [0] * (n * 2 + 1)
    result = 0

    for a in alist:
        update(segtree, n, a)
        result += count(segtree, n, a)

    print(result)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
