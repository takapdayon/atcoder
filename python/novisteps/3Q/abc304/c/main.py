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

def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def main():
    N, D = map(int, input().split())
    XYN = [list(map(int, input().split())) for _ in range(N)]
    infected = [False] * (N)
    infected[0] = True
    queue = deque()
    queue.append((XYN[0][0], XYN[0][1]))

    while queue:
        nx, ny = queue.popleft()
        for i, (x, y) in enumerate(XYN):
            if infected[i]:
                continue
            if distance(x, y, nx, ny) <= D:
                infected[i] = True
                queue.append((x, y))

    for infe in infected:
        print(infe and 'Yes' or 'No')

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
