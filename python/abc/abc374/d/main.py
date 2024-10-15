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

def distance(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def dfs(node, N, visited, graph, memo, S, T):

    visited[node] = True
    result = 0

    if node < N:
        # AB->CD
        ab = memo[node]
        cd = memo[node + N]
        result += distance(ab[0], ab[1], cd[0], cd[1]) / T
        visited[node + N] = True
    else:
        # CD->AB
        ab = memo[node - N]
        cd = memo[node]
        result += distance(ab[0], ab[1], cd[0], cd[1]) / T
        visited[node - N] = True

    if all(visited):
        return result

    tmp = 10 ** 19
    for to in graph[node]:
        if visited[to]:
            continue
        value = dfs(to, N, deepcopy(visited), graph, memo, S, T)

        tmp = min(tmp, value + distance(memo[node][0], memo[node][1], memo[to][0], memo[to][1]) / S)

    return result + tmp

def main():
    N, S, T = i_map()
    ABCDN = i_row_list(N)

    memo = {}
    for i, (A, B, C, D) in enumerate(ABCDN):
        memo[i] = (A, B)
        memo[i + N] = (C, D)

    graph = defaultdict(set)
    for i in range(N * 2):
        for w in range(N * 2):
            if i == w:
                continue
            graph[i].add(w)

    result = 10 ** 20

    for i in range(N):
        visited = [False] * (N * 2)
        result = min(result, dfs(i, N, visited, graph, memo, S, T))

    for i in range(N):
        visited = [False] * (N * 2)
        result = min(result, dfs(i + N, N, visited, graph, memo, S, T))

    print(sqrt(result))

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
