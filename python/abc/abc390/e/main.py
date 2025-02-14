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

def check(mid, N, X, VACN):
    # 1, 2, 3でmidを作ったときXを超えないか
    vs = [[], [], []]
    cal = 0
    for v, a, c in VACN:
        heappush(vs[v - 1], (c / a, a, c))

    for i in range(3):
        score = 0
        while score <= mid and vs[i]:
            val = heappop(vs[i])
            score += val[1]
            cal += val[2]
    return cal < X

def main():
    N, X = i_map()
    VACN = i_row_list(N)

    ok = 0
    ng = 10 ** 9
    while abs(ng - ok) > 1:
        mid = (ng + ok) // 2
        if check(mid, N, X, VACN):
            ok = mid
        else:
            ng = mid
    print(ok)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
