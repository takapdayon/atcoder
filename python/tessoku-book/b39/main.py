import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial, atan, degrees
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
def s_row_list(N): return [s_list() for _ in range(N)]

sys.setrecursionlimit(10 ** 6)

INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():
    n, d = i_map()
    xyrows = i_row_list(n)
    st_xyrows = sorted(xyrows)
    st_xrows = [xy[0] for xy in st_xyrows]

    result = 0
    wk = [True] * n

    for i in range(1, d + 1):
        max_mon = 0
        index = -1
        end = bisect_right(st_xrows, i)
        for w in range(end):
            if wk[w] and max_mon < st_xyrows[w][1]:
                max_mon = st_xyrows[w][1]
                index = w

        result += max_mon
        wk[index] = (index == -1 and True) or False

    print(result)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
