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
    nc = s_map()
    alist = s_input()

    '''
    全探索するなら:
        最後からalistの文字サイズになるまであり得る分岐を全列挙する
    Blueで終わる場合:
        w+b or r+rしかありえない
    Redで終わる場合:
        b+b or w+rしかありえない
    Whiteで終わる場合:
        w+w or b+rしかありえない
    '''
    count = 0

    for a in alist:
        if a == 'R':
            count += 2
        if a == 'B':
            count += 1

    if count % 3 == 0 and nc[1] == 'W':
        print('Yes')
        return

    if count % 3 == 1 and nc[1] == 'B':
        print('Yes')
        return

    if count % 3 == 2 and nc[1] == 'R':
        print('Yes')
        return
    print('No')

if __name__ == '__main__':
    main()

# テスト: oj t -c 'python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
