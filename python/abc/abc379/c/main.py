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
    XM = i_list()
    AM = i_list()
    XM = [i - 1 for i in XM]
    XM.append(N)
    AM.append(1)
    result = 0
    memo = defaultdict(int)
    memo[XM[0]] = AM[0] - 1

    for i in range(1, M + 1):
        memo[XM[i]] = AM[i] - 1
        diff_m = XM[i] - XM[i - 1] - 1
        count = diff_m
        result += (diff_m * (diff_m + 1)) // 2
        i_i = i - 1
        while count != 0:
            if i_i < 0:
                print(-1)
                return
            if count - memo[XM[i_i]] <= 0:
                result += ((i - 1) - i_i) * count
                memo[XM[i_i]] -= count
                count = 0
            else:
                result += ((i - 1) - i_i) * memo[XM[i_i]]
                count -= memo[XM[i_i]]
                memo[XM[i_i]] = 0
            i_i -= 1

    print(result)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
