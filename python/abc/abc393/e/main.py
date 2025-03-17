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

# ref: https://algo-method.com/descriptions/84
@cache
def calc_divisors(N):
    res = []
    for i in range(1, N + 1):
        if i * i > N:
            break

        if N % i != 0:
            continue

        res.append(i)

        if N // i != i:
            res.append(N // i)

    res.sort()
    return res

def ddfs(cur_idx, cur_val)

def main():
    N, K = i_map()
    AN = i_list()

    memo = defaultdict(int)
    divisors = []
    for a in AN:
        div = calc_divisors(a)
        for d in div:
            memo[d] += 1
        divisors.append(div)

    for i, a in enumerate(AN):
        current = len(divisors[i]) - 1
        while True:
            if memo[divisors[i][current]] >= K:
                break
            current -= 1
        print(divisors[i][current])

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
