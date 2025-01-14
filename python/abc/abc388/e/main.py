import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial, atan, degrees
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce, cache
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
def s_row_list(N): return [list(s_input()) for _ in range(N)]

sys.setrecursionlimit(10 ** 6)

INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def left(N, AN):
    memo = defaultdict(int)
    for a in AN:
        memo[a] += 1
    _sum = 0
    left = 0
    for a in AN:
        if not memo.get(a, 0):
            continue

        i = bisect_left(AN, a * 2)
        if i < left:
            i = left
        if i == N:
            continue

        while i != N:
            val = AN[i]
            if memo.get(val, 0):
                break
            i += 1
        else:
            continue
        left = i

        _sum += 1
        memo[a] -= 1
        memo[val] -= 1
    return _sum

def right(N, AN):
    memo = defaultdict(int)
    for a in AN:
        memo[a] += 1
    _sum = 0
    right = N
    for a in reversed(AN):
        if not memo.get(a, 0):
            continue

        i = bisect_right(AN, a // 2)
        if i > right:
            i = right
        if i == 0:
            continue
        while i != 0:
            val = AN[i - 1]
            if memo.get(val, 0):
                break
            i -= 1
        else:
            continue
        right = i

        _sum += 1
        memo[a] -= 1
        memo[val] -= 1
    return _sum

def main():
    N = i_input()
    AN = i_list()

    print(max(left(N, AN), right(N, AN)))

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
