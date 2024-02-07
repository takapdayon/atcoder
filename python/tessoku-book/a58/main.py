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

def update(segtree, n, pos, x):
    cur = pos + n - 1
    segtree[cur] = x
    while True:
        cur //= 2
        if cur == 0:
            break
        segtree[cur] = max(segtree[cur * 2], segtree[cur * 2 + 1])

def maximum(segtree, n, l, r):
    l += n - 1
    r += n - 1
    max_v = 0
    while l < r:
        if l % 2 == 1:
            max_v = max(max_v, segtree[l])
            l += 1
        l //= 2
        if r % 2 == 1:
            max_v = max(max_v, segtree[r - 1])
            r -= 1
        r //= 2
    return max_v

def main():
    n, q = i_map()
    queries = i_row_list(q)
    segtree = [0] * (n * 2 + 1)

    for query in queries:
        if query[0] == 1:
            update(segtree, n, query[1], query[2])
        else:
            max_v = maximum(segtree, n, query[1], query[2])
            print(max_v)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
