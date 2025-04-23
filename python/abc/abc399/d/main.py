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
    T = i_input()
    result = [0] * T

    for t in range(T):
        N = i_input()
        AN = i_list()
        count = 0

        memo = defaultdict(int)
        done = defaultdict(bool)

        if N == 1:
            result[t] = 0
            continue

        for i in range(N * 2):
            if (i != 0 and AN[i] == AN[i - 1]) or (i != N * 2 - 1 and AN[i] == AN[i + 1]):
                continue
            if i != 0 :
                key = (min(AN[i], AN[i - 1]), max(AN[i], AN[i - 1]))
                if AN[i] > AN[i - 1]:
                    memo[key] += 1
                if not done[key] and memo[key] == 2:
                    count += 1
                    done[key] =True
            if i != N * 2 - 1:
                key = (min(AN[i], AN[i + 1]), max(AN[i], AN[i + 1]))
                if AN[i] > AN[i + 1]:
                    memo[key] += 1
                if not done[key] and memo[key] == 2:
                    count += 1
                    done[key] =True

        result[t] = count

    for r in result:
        print(r)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
