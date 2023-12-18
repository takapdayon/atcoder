import sys, re
from math import ceil, floor, sqrt, pi, factorial, atan, degrees
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
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)

sys.setrecursionlimit(10 ** 6)

INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():
    n = i_input()
    arow = i_list()
    brow = i_list()
    crow = i_list()

    result = 0
    a46 = defaultdict(int)
    b46 = defaultdict(int)
    c46 = defaultdict(int)

    for a in arow:
        lack_value = a % 46
        a46[lack_value] += 1

    for b in brow:
        lack_value = b % 46
        b46[lack_value] += 1

    for c in crow:
        lack_value = c % 46
        c46[lack_value] += 1

    for ak, av in a46.items():
        for bk, bv in b46.items():
            for ck, cv in c46.items():
                if (ak + bk + ck) % 46 == 0:
                    result += av * bv * cv

    print(result)

if __name__ == '__main__':
    main()
