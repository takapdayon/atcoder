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

    # dist = [ 10 ** 18 ] * (N + 1)
    # dist[VK[0]] = 0

    # graph = defaultdict(set)
    # for a, b in ABN:
    #     graph[a].add(b)
    #     graph[b].add(a)

    # visited = [False] * (N + 1)
    # q = []

    # heappush(q, (1, VK[0]))

    # while q:
    #     d, now = heappop(q)
    #     if visited[now]:
    #         continue

    #     visited[now] = True

    #     for to in graph[now]:
    #         if dist[now] + 1 < dist[to]:
    #             dist[to] = dist[now] + 1
    #             heappush(q, (dist[to], to))

    # print(max([dist[vk] for vk in VK]))

def dfs(node, visited, graph, VK_s):

    visited[node] = True

    # 終了
    if all([visited[to] for to in graph[node]]):
        if node in VK_s:
            return 1
        return 0

    res = 0
    for to in graph[node]:
        if visited[to]:
            continue
        res += dfs(to, visited, graph, VK_s)
    if node in VK_s or res != 0:
        return res + 1
    return res


def main():
    N, K = i_map()
    ABN = i_row_list(N - 1)
    VK = i_list()
    VK_s = set(VK)

    graph = defaultdict(set)
    for a, b in ABN:
        graph[a].add(b)
        graph[b].add(a)

    visited = [False] * (N + 1)

    result = dfs(VK[0], visited, graph, VK_s)

    print(result)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
