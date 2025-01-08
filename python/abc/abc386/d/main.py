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
def s_row_list(N): return [list(s_map()) for _ in range(N)]

sys.setrecursionlimit(10 ** 6)

INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():
    N, M = i_map()
    XYC = s_row_list(M)
    memo_w = defaultdict(SortedSet)
    memo_b = defaultdict(SortedSet)
    sy_w = SortedSet()
    sy_b = SortedSet()
    sy_m_w = {}
    sy_m_b = {}

    for x, y, c in XYC:
        x = int(x)
        y = int(y)
        if c == 'W':
            h_b = memo_b.get((x, 'h'), SortedSet())
            if h_b.bisect_left(x) != len(h_b):
                print("No")
                return
            w_b = memo_b.get((y, 'w'), SortedSet())
            if w_b.bisect_left(y) != len(w_b):
                print("No")
                return
            i = sy_b.bisect_left(x)
            if i != len(sy_b):
                if sy_m_b[sy_b[i]] > y:
                    print("No")
                    return
            memo_w[(x, 'h')].add((y))
            memo_w[(y, 'w')].add((x))
            i = sy_w.bisect_left(x)
            if i != len(sy_w):
                sy_m_w[x] = max(y, sy_m_w[sy_w[i]])
            else:
                sy_m_w[x] = y
            sy_w.add(x)

        else:
            h_w = memo_w.get((x, 'h'), SortedSet())
            if h_w.bisect_left(x) != 0:
                print("No")
                return
            w_w = memo_w.get((y, 'w'), SortedSet())
            if w_w.bisect_left(y) != 0:
                print("No")
                return
            i = sy_w.bisect_left(x)
            if i != 0:
                if sy_m_w[sy_w[i - 1]] > y:
                    print("No")
                    return
            memo_b[(x, 'h')].add((y))
            memo_b[(y, 'w')].add((x))
            i = sy_b.bisect_left(x)
            if i != 0:
                sy_m_b[x] = max(y, sy_m_b[sy_b[i - 1]])
            else:
                sy_m_b[x] = y
            sy_b.add(x)

    print("Yes")

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
