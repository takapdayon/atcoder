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
    n, k = i_map()
    abrows = i_row_list(n)

    '''
    全探索するなら:
        2人になる組み合わせ2**nを試す。まぁbit全探索で取りえる組み合わせすべてを網羅する感じ。
        当然Nが300まであるので間に合わない
    どうする:
        累積和で0~100までの人数をかき集めて、iの状態の差分をとる。
        差分はi - 30 < i < i + 30までの間
        体力気力どちらも上記を行い、minで低い側のmaxをとる
    '''
    c_sum = [[0] * 101 for _ in range(101)]
    k += 1

    for a, b in abrows:
        c_sum[a][b] += 1
        if b + k <= 100:
            c_sum[a][b + k] -= 1
        if a + k <= 100:
            c_sum[a + k][b] -= 1
        if b + k <= 100 and a + k <= 100:
            c_sum[a + k][b + k] += 1

    for h in range(1, 101):
        for w in range(1, 101):
            c_sum[h][w] += c_sum[h][w - 1]

    for w in range(1, 101):
        for h in range(1, 101):
            c_sum[h][w] += c_sum[h - 1][w]

    result = max([max(c) for c in c_sum])
    print(result)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
