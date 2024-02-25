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
    N, W = i_map()
    wvrows = i_row_list(N)
    V = (10 ** 3) * N
    '''
    dとほぼ同じだけど、x軸は重さだと10**9で間に合わないので価値にする
    価値vとして重さをとりえれるかを見て、あり得る重さになったときが最大価値とする
    '''
    dp = [[ 10 ** 19 ] * (V + 1) for _ in range(N + 1)]
    dp[0][0] = 0

    for h in range(1, N + 1):
        for w in range(V + 1):
            if w < wvrows[h - 1][1]:
                dp[h][w] = dp[h - 1][w]
                continue
            dp[h][w] = min(dp[h - 1][w], dp[h - 1][w - wvrows[h - 1][1]] + wvrows[h - 1][0])

    # あり得る最大価値になったら出力して終了
    for w in reversed(range(1, V + 1)):
        if dp[N][w] > W:
            continue
        print(w)
        return

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
