import sys, re
from math import ceil, floor, sqrt, pi, gcd, factorial, atan, degrees
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
    n, m = i_map()
    xlist = i_list()

    result = 10 ** 9
    '''
    1-2-3-4-5-6-7-1のようになっていて、遠回りと近道の2択がある。壊される橋が遠回り側なら問題はない
    全探索するなら:
        全探索するなら頂点Mから次の頂点まで、1~nまでの橋を壊したときの最小値を求める
        でも全探索すると10 ** 5 * 10 ** 5 = 10 ** 10くらいで間に合わない
    どうする:
        うーん...
    '''

if __name__ == '__main__':
    main()
