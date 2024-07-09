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
    N = i_input()

    if N == 0:
        print('#')
        return

    if N == 1:
        print('###')
        print('#.#')
        print('###')
        return

    matrix = [['#'] * (3 ** N) for _ in range(3 ** N)]
    for i in range(N):
        max_count = 3 ** i
        h_f = True
        for h in range(3 ** N):
            w_f = True
            if max_count <= h % (3 ** (i + 1)) < (max_count * 2):
                h_f = True
            else:
                h_f = False
            for w in range(3 ** N):
                if max_count <= w % (3 ** (i + 1)) < (max_count * 2):
                    w_f = True
                else:
                    w_f = False
                if h_f and w_f:
                    matrix[h][w] = '.'
    for m in matrix:
        print(''.join(m))

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
