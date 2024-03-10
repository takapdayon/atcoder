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

def dfs():
    pass

def main():
    t = s_input()
    t_len = len(t)
    n = i_input()
    m_box = s_row_str(n)
    '''
    dp[i][j] = 最小のコスト
    i = 1~Nまでの袋
    j = 1~t_lenまでの文字列
    '''
    dp = [[INF] * (t_len + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(t_len + 1):
            dp[i][j] = min(dp[i - 1][j], dp[i][j])

            # そもそも前回から作れないなら終わり
            if dp[i - 1][j] == INF:
                continue

            # わんちゃんあるなら文字列結合して比較
            for mozi in m_box[i - 1][1:]:
                mozi_len = len(mozi)

                # 文字超えるならばいばい
                if j + mozi_len > t_len:
                    continue

                # 一致しないならばいばい
                if t[:j + mozi_len] != t[:j] + mozi:
                    continue

                dp[i][j + mozi_len] = min(dp[i][j + mozi_len], dp[i - 1][j] + 1)

    if dp[n][t_len] == INF:
        print(-1)
    else:
        print(dp[n][t_len])

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
