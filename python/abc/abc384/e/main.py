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

NEXT = list(zip([1, 0, -1, 0], [0, -1, 0, 1]))

def main():
    H, W, X = i_map()
    P, Q = i_map()
    SHW = i_row_list(H)

    power = SHW[P - 1][Q - 1]

    visited = [[False] * W for _ in range(H)]
    is_taka = [[False] * W for _ in range(H)]
    is_taka[P - 1][Q - 1] = True

    q = []

    heappush(q, (power, (P - 1, Q - 1)))

    while q:
        slime, now = heappop(q)
        if visited[now[0]][now[1]]:
            continue

        visited[now[0]][now[1]] = True

        flag = False
        for nhi, nwi in NEXT:
            nh, nw = nhi + now[0], nwi + now[1]
            if nh < 0 or nw < 0 or nh >= H or nw >= W:
                continue
            if is_taka[nh][nw]:
                flag = True
                break

        if flag:
            if slime < (power / X):
                power += slime
                is_taka[now[0]][now[1]] = True

        for nhi, nwi in NEXT:
            nh, nw = nhi + now[0], nwi + now[1]
            if nh < 0 or nw < 0 or nh >= H or nw >= W:
                continue
            heappush(q, (SHW[nh][nw], (nh, nw)))

    print(power)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
