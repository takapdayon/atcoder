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
    UVTM = i_row_list(M)
    Q = i_input()
    '''
    ダイクストラで、絶対通る必要があるコストを0にする
    '''

    graph = defaultdict(set)
    path = defaultdict(set)
    cost = {}
    for i, (U, V, T) in enumerate(UVTM, 1):
        path[(U, V)].add(i)
        path[(V, U)].add(i)
        cost[i] = T
        graph[U].add(V)
        graph[V].add(U)

    for q in range(Q):
        K = i_input()
        BK = i_list()
        set_BK = set(BK)
        non_through = {}

        ne_cost = sum([cost[b] for b in BK])

        dist = [ 10 ** 18 ] * (N + 1)
        dist[1] = 0

        visited = [False] * (N + 1)
        q = []

        heappush(q, (dist[1], 1, False))

        while q:
            d, now, cost_zero = heappop(q)
            if visited[now] and not cost_zero:
                continue

            visited[now] = True

            for to in graph[now]:
                # toへ行くための最小値
                _p = set_BK & path[(now, to)]
                min_cost = min([cost[nt] for nt in path[(now, to)]])
                for p in _p:
                    if non_through.get(p, True):
                        min_cost = 0
                        non_through[p] = False

                if dist[now] + min_cost < dist[to]:
                    dist[to] = dist[now] + min_cost
                    heappush(q, (dist[to], to, min_cost == 0))

        print(dist[N] + ne_cost)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
