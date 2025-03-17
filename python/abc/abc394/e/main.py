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

def dfs(h, w, idx, visited, CNN, queue, graph):
    visited[idx] = True

    if w == idx:
        s = "".join(queue)
        if s == s[::-1]:
            return len(s)

        if CNN[h][h] != '-':
            queue.appendleft(CNN[h][h])
            s = "".join(queue)
            queue.popleft()
            if s == s[::-1]:
                return len(s)
        if CNN[w][w] != '-':
            queue.append(CNN[w][w])
            s = "".join(queue)
            queue.pop()
            if s == s[::-1]:
                return len(s)
        return 100

    t = 100
    for to in graph[idx]:
        if visited[to]:
            continue
        queue.append(CNN[idx][to])
        val = dfs(h, w, to, visited, CNN, queue, graph)
        t = min(t, val)
        queue.pop()
    return t

def main():
    N = i_input()
    CNN = s_row_list(N)
    results = []

    graph = defaultdict(set)
    for h in range(N):
        for w in range(N):
            if h == w:
                continue
            if CNN[h][w] != '-':
                graph[h].add(w)

    for h in range(N):
        tmp = [-1] * N
        for w in range(N):
            # 自分自身は空文字扱い
            if h == w:
                tmp[w] = 0
                continue
            # 文字があれば最短で1
            if CNN[h][w] != '-':
                tmp[w] = 1
                continue
            ff = 100
            for to in graph[h]:
                visited = [False] * N
                visited[h] = True
                val = dfs(h, w, to, visited, CNN, deque(CNN[h][to]), graph)
                ff = min(ff, val)

            if ff != 100:
                tmp[w] = ff

        results.append(tmp)

    for result in results:
        print(*result)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
