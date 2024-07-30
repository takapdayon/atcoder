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
    H, W, Y = i_map()
    AHW = i_row_list(H)

    result = H * W
    sank = [[False] * W for _ in range(H)]
    year = [[] for _ in range(Y)]

    for h in range(H):
        for w in range(W):
            if AHW[h][w] <= Y:
                year[AHW[h][w] - 1].append((h, w))

    for i, y in enumerate(year, 1):
        queue = deque(y)
        while queue:
            now = queue.popleft()
            if sank[now[0]][now[1]]:
                continue

            for nhi, nwi in zip([1, 0, -1, 0], [0, -1, 0, 1]):
                nh, nw = now[0] + nhi, now[1] + nwi
                if nh < 0 or nh >= H or nw < 0 or nw >= W or sank[nh][nw]:
                    sank[now[0]][now[1]] = True
                    result -= 1
                    break

            if sank[now[0]][now[1]]:
                for nhi, nwi in zip([1, 0, -1, 0], [0, -1, 0, 1]):
                    nh, nw = now[0] + nhi, now[1] + nwi
                    if nh < 0 or nh >= H or nw < 0 or nw >= W or sank[nh][nw]:
                        continue
                    if AHW[nh][nw] <= i:
                        queue.append((nh, nw))

        print(result)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
