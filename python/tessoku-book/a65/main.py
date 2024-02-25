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


def dfs(graph, visited, count, node):
    # 来た事あるなら0を返す
    if visited[node]:
        return 0

    visited[node] = True
    # ないのであれば、子ノードからreturnされる値を足し合わせて自分のに加え、自分をプラスして上に返す
    subordinate = 0
    for to in graph[node]:
        subordinate += dfs(graph, visited, count, to)
    count[node] = subordinate
    return subordinate + 1

def main():
    n = i_input()
    alist = i_list()

    graph = defaultdict(list)
    visited = [False] * (n + 1)

    count = [0] * (n + 1)

    for i, a in enumerate(alist, 2):
        graph[i].append(a)
        graph[a].append(i)

    count[1] = dfs(graph, visited, count, 1) - 1

    print(*count[1:])

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
