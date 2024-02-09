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

def main():
    r, c = i_map()
    start = i_list()
    goal = i_list()
    squares = s_row_list(r)
    breadths = [[0] * c for _ in range(r)]
    visited = [[False] * c for _ in range(r)]
    visited[start[0] - 1][start[1] - 1] = True

    queue = deque()
    queue.append(start)

    while queue:
        now = queue.popleft()
        # 上下左右で行ける場所を探す
        for to in [[now[0] + 1, now[1]], [now[0] - 1, now[1]], [now[0], now[1] + 1], [now[0], now[1] - 1]]:
            if squares[to[0] - 1][to[1] - 1] != '#' and not visited[to[0] - 1][to[1] - 1]:
                queue.append(to)
                visited[to[0] - 1][to[1] - 1] = True
                breadths[to[0] - 1][to[1] - 1] = breadths[now[0] - 1][now[1] - 1] + 1

    print(breadths[goal[0] - 1][goal[1] - 1])

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
