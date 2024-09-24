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
a_count = 0
num_list = []
str_list = []

def dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def create_A(node, visited, G, A):
    global a_count
    for to in G[node]:
        if visited[to]:
            continue
        A[a_count] = to
        a_count += 1
        visited[to] = True
        create_A(to, visited, G, A)

def main():
    # get input
    N, M, T, L_A, L_B = map(int, input().split())

    G = [[] for _ in range(N)]

    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    t = list(map(int, input().split()))

    P = []
    for _ in range(N):
        x, y = map(int, input().split())
        P.append((x, y))

    # construct and output the array A
    visited = [False] * N
    A = [0] * L_A
    create_A(0, visited, G, A)
    print(*A)

    B = A[:L_B]

    pos_from = 0

    for pos_to in t:

        # determine the path by DFS
        path = []
        visited = [False] * N

        def dfs(cur, prev):
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

        dfs(pos_from, -1)

        # for every step in the path, control the signal and move
        for u in path:
            if u not in B:
                index_u = A.index(u)
                before_count = 0
                after_count = 0
                for b_p in A[max(0, index_u - L_B):index_u]:
                    if b_p in path:
                        before_count += 1

                for a_p in A[index_u:index_u + L_B]:
                    if a_p in path:
                        after_count += 1

                B = before_count < after_count and A[index_u:index_u + L_B] or A[max(0, index_u - L_B + 1):index_u + 1]
                print('s', min(L_B, N - index_u + L_B), before_count < after_count and index_u or max(0, index_u - L_B), 0)
                print('m', u)
            else:
                print('m', u)

        pos_from = pos_to

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
