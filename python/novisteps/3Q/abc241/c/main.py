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

_NH = [1, 1, 0, -1, -1, -1, 0, 1]
_NW = [0, -1, -1, -1, 0, 1, 1, 1]

def main():
    N = int(input())
    SN = [list(input()) for _ in range(N)]

    for h in range(N):
        for w in range(N):
            for nhi, nwi in zip(_NH, _NW):
                count = SN[h][w] == '#' and 1 or 0
                enough = True
                for i in range(1, 6):
                    nh, nw = h + (nhi * i), w + (nwi * i)
                    if nh < 0 or nh >= N or nw < 0 or nw >= N:
                        enough = False
                        continue
                    count += SN[nh][nw] == '#' and 1 or 0
                if count >= 4 and enough:
                    print('Yes')
                    return

    print('No')

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
