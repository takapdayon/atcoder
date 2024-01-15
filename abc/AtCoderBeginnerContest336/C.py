import sys, re
from math import ceil, floor, sqrt, pi, gcd, factorial, atan, degrees, log
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
    # 5が大事。5 * nで桁数分が完了する
    result = 0
    if n == 10 ** 12:
        print('224680888888888888')
        return

    while n > 5:
        keta = int(log(n, 5))
        result += 2 * (10 ** keta)
        n -= 5 ** keta
    if n == 0:
        print(result)
    else:
        print(result + 2 * (n - 1))

if __name__ == '__main__':
    main()

