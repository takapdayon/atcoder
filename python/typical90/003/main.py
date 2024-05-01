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

def dfs(node, graph, visited):

    if visited[node]:
        return 0

    visited[node] = True

    ret = 0
    for to in graph[node]:
        if visited[to]:
            continue
        ret = max(ret, dfs(to, graph, visited))

    return ret + 1

def main():
    N = i_input()
    abrows = i_row_list(N - 1)
    graph = defaultdict(set)
    for a, b in abrows:
        graph[a].add(b)
        graph[b].add(a)

    start = (1, 0)
    queue = deque()
    visited = [False] * (N + 1)
    queue.append(start)
    while queue:
        now, index = queue.popleft()
        visited[now] = True
        if start[1] < index:
            start = (now, index)
        for to in graph[now]:
            if visited[to]:
                continue
            queue.append((to, index + 1))

    visited = [False] * (N + 1)
    result = dfs(start[0], graph, visited)
    print(result)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
