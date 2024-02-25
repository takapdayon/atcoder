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

def de_get(segtree, n, pos):
    cur = pos + n - 1
    ret = segtree[cur]
    segtree[cur] = 0
    while True:
        d = cur % 2
        cur //= 2
        if cur == 0:
            break
        ret += segtree[cur]
        if d:
            segtree[cur * 2] += segtree[cur]
        else:
            segtree[cur * 2 + 1] += segtree[cur]
        segtree[cur] = 0
    return ret

def get(segtree, n, pos):
    cur = pos + n - 1
    ret = segtree[cur]
    while True:
        cur //= 2
        if cur == 0:
            break
        ret += segtree[cur]
    return ret

def update(segtree, n, pos, balls):
    '''
    受け取ったpos + balls分まで+1、もしはみ出すなら余剰分は0から
    '''
    over = (pos + balls) // n
    le = n + pos - 1
    ri = (pos + balls) % n - 1

    if over >= 1:
        if le <= ri:
            segtree[1] += over
            over = 0

    if over:
        ri = n * 2
        while le < ri:
            if le % 2 == 1:
                segtree[le] += 1
                le += 1
            le //= 2
            if ri % 2 == 1:
                segtree[ri - 1] += 1
                ri -= 1
            ri //= 2

        le = n
        ri = (pos + balls) % n - 1
        while le < ri:
            if le % 2 == 1:
                segtree[le] += 1
                le += 1
            le //= 2
            if ri % 2 == 1:
                segtree[ri - 1] += 1
                ri -= 1
            ri //= 2

    else:
        while le < ri:
            if le % 2 == 1:
                segtree[le] += 1
                le += 1
            le //= 2
            if ri % 2 == 1:
                segtree[ri - 1] += 1
                ri -= 1
            ri //= 2

def main():
    n, m = i_map()
    alist = i_list()
    blist = i_list()

    """
    考え方:
    取り出した玉を+1ずつ配っていく。ただNを超えるなら0から
    難しい点:
    更新するコストが高い。imosは途中結果を知りたいから無理。
    どうする:
    RAQを使って区間更新、1点取得
    """
    segtree = [0] * (n + 1)
    segtree.extend(alist)

    for b in blist:
        balls = de_get(segtree, n, b + 1)
        update(segtree, n, b + 1, balls)

    result = []
    for i in range(n):
        result.append(get(segtree, n, i))

    print(*result)

if __name__ == '__main__':
    main()
