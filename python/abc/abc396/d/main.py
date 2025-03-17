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
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

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

def dfs(node, graph, label, visited, xor = None):
    if node == len(visited) - 1:
        return xor

    res = 10 ** 50
    for to in graph[node]:
        if visited[to]:
            continue
        l = label[(node, to)]
        visited[to] = True
        res = min(res, dfs(to, graph, label, visited, xor ^ l if xor is not None else l))
        visited[to] = False
    return res

def main():
    N, M = i_map()
    uvwM = i_row_list(M)
    graph = defaultdict(set)
    label = {}
    for u, v, w in uvwM:
        graph[u].add(v)
        graph[v].add(u)
        label[(u, v)] = w
        label[(v, u)] = w

    visited = [False] * (N + 1)
    visited[1] = True
    result = dfs(1, graph, label, visited)
    print(result)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
