import sys, re
from math import ceil, floor, sqrt, pi, gcd, factorial, atan, degrees
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

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
def s_row_list(N): return [list(s_map()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)

sys.setrecursionlimit(10 ** 6)

INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():
    n = i_input()
    '''
    ステージNまで"最短"でどれくらい?
    各ステージをnode, かかる時間をedgesrangeだと考えてダイクストラ法
    '''

    dist = [ 10 ** 18 ] * (n + 1)
    dist[1] = 0

    graph = defaultdict(list)
    for i in range(1, n):
        a, b, x = i_map()
        graph[i].append([i + 1, a])
        graph[i].append([x, b])

    visited = [False] * (n + 1)
    q = []

    heappush(q, (dist[1], 1))

    while q:
        d, now = heappop(q)
        if visited[now]:
            continue

        visited[now] = True

        for e in graph[now]:
            if dist[now] + e[1] < dist[e[0]]:
                dist[e[0]] = dist[now] + e[1]
                heappush(q, (dist[e[0]], e[0]))

    print(dist[n])

if __name__ == '__main__':
    main()
