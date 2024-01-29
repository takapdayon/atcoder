import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial, atan, degrees
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
def s_row_list(N): return [s_list() for _ in range(N)]

sys.setrecursionlimit(10 ** 6)

INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():
    n = i_input()
    abrows = i_row_list(n)

    '''
    全探索するなら:
        bit全探索で全カードの組み合わせを列挙する。
        Nが10**5なので当然間に合わない
    どうする:
    '''
    p_ = 0
    _p = 0
    m_ = 0
    _m = 0

    for a, b in abrows:
        if a + b > 0:
            p_ += a + b
        if a - b > 0:
            _p += a - b
        if -a + b > 0:
            m_ += -a + b
        if -a - b > 0:
            _m += -a - b

    print(max(p_, _p, m_, _m))

if __name__ == '__main__':
    main()

# テスト: oj t -c 'python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
