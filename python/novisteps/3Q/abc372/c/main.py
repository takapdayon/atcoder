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
    N, Q = map(int, input().split())
    S = list(input())

    count = 0
    memo = {}

    for i in range(2, N):
        if f'{S[i - 2]}{S[i - 1]}{S[i]}' == 'ABC':
            count += 1
            memo[i - 2] = True
            memo[i - 1] = True
            memo[i] = True

    for q in range(Q):
        X, C = map(str, input().split())
        X = int(X) - 1

        if memo.get(X, False):
            count -= 1
            if S[X] == 'A':
                memo[X] = False
                memo[X + 1] = False
                memo[X + 2] = False
            elif S[X] == 'B':
                memo[X] = False
                memo[X + 1] = False
                memo[X - 1] = False
            else:
                memo[X] = False
                memo[X - 1] = False
                memo[X - 2] = False

        S[X] = C
        if C == 'A':
            if X < N - 2 and f'{S[X]}{S[X + 1]}{S[X + 2]}' == 'ABC':
                count += 1
                memo[X + 2] = True
                memo[X + 1] = True
                memo[X] = True

        elif C == 'B':
            if X < N - 1 and 1 <= X and f'{S[X - 1]}{S[X]}{S[X + 1]}' == 'ABC':
                count += 1
                memo[X - 1] = True
                memo[X + 1] = True
                memo[X] = True

        else:
            if 2 <= X and f'{S[X - 2]}{S[X - 1]}{S[X]}' == 'ABC':
                count += 1
                memo[X - 2] = True
                memo[X - 1] = True
                memo[X] = True

        print(count)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
