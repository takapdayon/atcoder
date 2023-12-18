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

def base10int(value, base):
    str_n = ''
    if value == 0:
        return "0"
    while value:
        if value % base >= 10:
            return -1
        str_n += str(value % base)
        value //= base
    return str_n[::-1]

INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():

    n, k = s_map()
    result = n

    for i in range(int(k)):
        ten = int(result, 8)
        nine = base10int(ten, 9)
        result = nine.replace("8", "5")

    print(result)

if __name__ == '__main__':
    main()
