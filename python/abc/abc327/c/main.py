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
    H = 9
    W = 9
    a_rows = i_row_list(H)

    result = True

    '''
    9 * 9ただ見ていくだけ
    '''
    for h in range(H):
        tmp = [0] * W
        for w in range(W):
            tmp[a_rows[h][w] - 1] += 1

        if max(tmp) != 1:
            result = False

    for w in range(W):
        tmp = [0] * H
        for h in range(H):
            tmp[a_rows[h][w] - 1] += 1
        if max(tmp) != 1:
            result = False

    # めんどいので足す
    su = [[0] * 3 for _ in range(3)]
    for h in range(H):
        for w in range(W):
            su[h // 3][w // 3] += a_rows[h][w]

    if min(su) != max(su):
        result = False

    print(result and 'Yes' or 'No')

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
