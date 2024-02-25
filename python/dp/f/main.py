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
    s = s_input()
    t = s_input()
    s_len = len(s)
    t_len = len(t)
    '''
    最長文字列を比較する
    貰うDPで上、左、斜め左 + 1のうち一番でかいのを保持する
    斜め左からの遷移はs[i] == t[j]の時のみ可能
    '''
    dp = [[0] * (s_len + 1) for _ in range(t_len + 1)]
    for h in range(1, t_len + 1):
        for w in range(1, s_len + 1):
            dp[h][w] = max(dp[h][w - 1], dp[h - 1][w])
            if s[w - 1] == t[h - 1]:
                dp[h][w] = max(dp[h][w], dp[h - 1][w - 1] + 1)

    '''
    最長文字サイズではなく、文字列を出力する必要があるのでdpから復元する
    '''
    result = ''
    cur_s = s_len
    cur_t = t_len
    while cur_s > 0 and cur_t > 0:
        if s[cur_s - 1] == t[cur_t - 1]:
            result += s[cur_s - 1]
            cur_s -= 1
            cur_t -= 1
        elif dp[cur_t - 1][cur_s] == dp[cur_t][cur_s]:
            cur_t -= 1
        else:
            cur_s -= 1

    print(result[::-1])

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
