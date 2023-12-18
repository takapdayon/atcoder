import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
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
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)

sys.setrecursionlimit(10 ** 6)

INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():
    n = i_input()
    abclist = i_list()
    abclist.sort(reverse=True)
    result = 10 ** 9

    for abc1 in range(n // abclist[0], -1, -1):
        tmp1 = (n - abclist[0] * abc1)
        for abc2 in range(tmp1 // abclist[1], -1, -1):
            tmp = tmp1 - abclist[1] * abc2
            if tmp % abclist[2] != 0:
                continue
            result = min(result, abc1 + abc2 + (tmp // abclist[2]))

    print(result)

if __name__ == '__main__':
    main()
