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
def s_row_list(N): return [s_list() for _ in range(N)]

sys.setrecursionlimit(10 ** 6)

INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():
    n, k = i_map()
    alist = i_list()
    '''
    alistをソートして、以下の2パターンを試す
    偶数: i jの差分合計を出力
    奇数: i j qの差分が最小になるjを抜いた合計を出力
    '''
    s_alist = sorted(alist)
    result = 0
    if k % 2 == 0:
        for i in range(0, k, 2):
            result += alist[i + 1] - alist[i]
    else:
        h_list = []
        t_list = []
        for i in range(1, k, 2):
            h_list.append(s_alist[i] - s_alist[i - 1])
            t_list.append(s_alist[i + 1] - s_alist[i])

        cur = sum(t_list)
        min_res = cur
        for i in range(k // 2):
            cur += h_list[i]
            cur -= t_list[i]
            min_res = min(min_res, cur)

        result += min_res

    print(result)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
