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
    AN = i_list()
    UVBM = i_row_list(M)

    dist = [ -1 ] * (N + 1)
    dist[1] = AN[0]
    graph = defaultdict(set)
    hev = {}

    for u, v, b in UVBM:
        graph[u].add(v)
        graph[v].add(u)
        hev[f'{u}:{v}'] = min(b, hev.get(f'{u}:{v}', 10 ** 18))
        hev[f'{v}:{u}'] = min(b, hev.get(f'{u}:{v}', 10 ** 18))

    visited = [False] * (N + 1)
    q = []

    heappush(q, (dist[1], 1))

    while q:
        d, now = heappop(q)
        if visited[now]:
            continue

        visited[now] = True

        for e in graph[now]:
            cost = dist[now] + hev[f'{e}:{now}'] + AN[e - 1]
            if cost < dist[e] or dist[e] == -1:
                dist[e] = cost
                heappush(q, (dist[e], e))

    for di in dist[2:]:
        print(di, end=' ')

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
