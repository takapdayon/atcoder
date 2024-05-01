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

def dfs(node, visited, ab, graph):

    if visited[node]:
        return

    visited[node] = True

    if ab[node] == -1:
        ab[node] = 0

    for to in graph[node]:
        if ab[to] == -1:
            ab[to] = (ab[node] + 1) % 2
            dfs(to, visited, ab, graph)

def main():
    N, M = i_map()
    alist = i_list()
    blist = i_list()
    graph = defaultdict(set)

    for m in range(M):
        graph[alist[m]].add(blist[m])
        graph[blist[m]].add(alist[m])

    ab = [-1] * (N + 1)

    visited = [False] * (N + 1)

    for n in range(N + 1):
        dfs(n, visited, ab, graph)

    result = True
    for i in range(M):
        if ab[alist[i]] == ab[blist[i]]:
            result = False

    print(result and 'Yes' or 'No')

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
