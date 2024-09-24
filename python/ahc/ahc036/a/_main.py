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

def dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


class SignalManager:
    def __init__(self) -> None:
        pass

    def change_signal(self):
        '''
        4≤LB≤24
        0, 1, 2, 3, 4, 5, 6

        '''
        pass


class PathManager:
    def __init__(self) -> None:
        pass

    def dfs():
        '''
        
        '''
        pass


def dfs(path, pos_from, pos_to, visited, cur, prev):
    if visited[cur]:
        return False

    if cur != pos_from:
        path.append(cur)

    visited[cur] = True
    if cur == pos_to:
        return True

    # visit next city in ascending order of Euclidean distance to the target city
    for v in sorted(G[cur], key=lambda x: dist(P[x], P[pos_to])):
        if v == prev:
            continue
        if dfs(v, cur):
            return True
    path.pop()
    return False

'''
1: 配列に入っているか
2: 今後使われるか
3: ある程度の範囲で変更してしまう
'''

from atcoder.dsu import DSU

class GraphManager:
    def __init__(self, uv, N) -> None:
        self.graph = defaultdict(set)
        for u, v in uv:
            self.connect_path(u, v)
        self._create_mini_graph(N)

    def _dfs(self, node, prev_node, uf):
        for to in self.graph[node]:
            if uf(node, to) and to != prev_node:
                self.disconnect_path(node, to)
            uf.merge(node, to)
            self._dfs(to, node, uf)

    def _create_mini_graph(self, N):
        uf = DSU(N)
        self._dfs(0, self.graph[0][0], uf)

    def connect_path(self, u, v):
        self.graph[u].add(v)
        self.graph[v].add(u)

    def disconnect_path(self, u, v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)

def create_AL(graph):


def main():
    N, M, T, LA, LB = i_map()
    uv = i_row_list(M - 1)
    tT = i_list()

    graph = GraphManager()

    A = [0] * LA
    B = [-1] * LB
    count = 0
    P = []
    for _ in range(N):
        x, y = map(int, input().split())
        P.append((x, y))

    # construct and output the array A
    A = list(range(LA))
    print(*A)

    pos_from = 0

    for pos_to in T:

        # determine the path by DFS
        path = []
        visited = [False] * N

        def dfs():


        dfs(pos_from, -1)

        # for every step in the path, control the signal and move
        for u in path:
            print('s', 1, u, 0)
            print('m', u)

        pos_from = pos_to

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
