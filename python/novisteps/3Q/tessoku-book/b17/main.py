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
    N = i_input()
    HN = i_list()
    dp = [10 ** 10] * N
    dp[0] = 0
    for i in range(1, N):
        dp[i] = min(dp[i], dp[i - 1] + abs(HN[i] - HN[i - 1]))
        if i >= 2:
            dp[i] = min(dp[i], dp[i - 2] + abs(HN[i] - HN[i - 2]))

    results = []
    current = N - 1
    while True:
        results.append(current + 1)
        if current == 0:
            break
        if dp[current - 1] + abs(HN[current] - HN[current - 1]) == dp[current]:
            current -= 1
        else:
            current -= 2

    print(len(results))
    print(*reversed(results))

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
