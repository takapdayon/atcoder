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

nodes = []
graph = defaultdict(list)

@cache
def search(index):
    global nodes
    global graph

    node = nodes[index]
    if node:
        return
    nodes[index] = True
    tos = graph[index]
    for to in tos:
        search(to)

def main():
    global nodes
    global graph

    n, m = i_map()
    nodes = [False] * (n + 1)
    nodes[0] = True

    for _ in range(m):
        a, b = i_map()
        graph[a].append(b)
        graph[b].append(a)

    # 深さ優先探索開始~
    search(1)

    print(all(nodes) and 'The graph is connected.' or 'The graph is not connected.')

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
