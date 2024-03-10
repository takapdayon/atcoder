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

def dfs(node, graph, visited):
    visited[node] = True
    count = 0
    for to in graph[node]:
        if not visited[to]:
            count += dfs(to, graph, visited)
    return count + 1

def main():
    n = i_input()
    graph = defaultdict(set)
    for i in range(n - 1):
        u, v = i_map()
        graph[u].add(v)
        graph[v].add(u)
    '''
    ノードの下何個で削除できるのかDFSで掘って、一番大きいもののみ残す
    '''
    visited = [False] * (n + 1)
    visited[1] = True

    result = 0
    max_res = 0

    for to in graph[1]:
        cost = dfs(to, graph, visited)
        result += cost
        max_res = max(max_res, cost)

    print(result + 1 - max_res)

if __name__ == '__main__':
    main()

'''
テスト: oj t -c 'poetry run python main.py'
提出: acc s main.py -- --guess-python-interpreter pypy
再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
又は
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
'''