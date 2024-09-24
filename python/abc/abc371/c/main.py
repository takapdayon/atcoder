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

def same(count_MG):
    pass

def main():
    N = i_input()
    MG = i_input()
    uvMG = i_row_list(MG)
    graph_MG = defaultdict(set)

    for u, v in uvMG:
        graph_MG[u].add(v)
        graph_MG[v].add(u)

    count_MG = [0] * (N + 1)
    for i in range(1, N + 1):
        count_MG[i] = len(graph_MG[i])

    MH = i_input()
    abMH = i_row_list(MH)
    graph_MH = defaultdict(set)

    for a, b in abMH:
        graph_MH[a].add(b)
        graph_MH[b].add(a)

    count_MH = [0] * (N + 1)
    for i in range(1, N + 1):
        count_MH[i] = len(graph_MH[i])

    ANN = i_row_list(N - 1)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
