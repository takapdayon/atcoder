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

def main():
    N, M = i_map()
    AN = i_list()
    BM = i_list()

    memo = {}
    _min = 10 ** 19
    _min_i = 0
    for i, a in enumerate(AN, 1):
        if _min <= a:
            memo[a] = _min_i
        else:
            _min_i = i
            _min = a
            memo[a] = i

    i_memo = {}
    for i, a in enumerate(AN, 1):
        if not i_memo.get(a, False):
            i_memo[a] = i
    s_AN = sorted(AN)

    for b in BM:
        l_index = bisect_left(s_AN, b)
        r_index = bisect_right(s_AN, b)

        if r_index == 0:
            print(-1)
            continue

        if l_index == 0:
            val = s_AN[r_index - 1]
            print(memo[val])
            continue

        if l_index == r_index:
            val = s_AN[r_index - 1]
            print(memo[val])
            continue

        l_val = s_AN[l_index - 1]
        r_val = s_AN[r_index - 1]
        i_min = l_val if i_memo[l_val] < i_memo[r_val] else r_val
        print(memo[i_min])

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055

# 3 5
# 3 8 2
# 5 2 6 8 10 2 1
