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
    H, W = i_map()
    arows = s_row_list(H)
    N = i_input()
    rcerows = i_row_list(N)
    '''
    BFSで対象Tに移動できるか判定
    薬があるか判定し、ある、かつエネルギーが現状より多いなら使う
    0 or 行くとこなくなったら終了
    目標Tでも終了
    '''
    # エネルギーは絶対0貰えるようにしよう
    es = {}
    start = []
    end = []
    for r, c, e in rcerows:
        es[f'{r - 1}{c - 1}'] = e

    for h in range(H):
        for w in range(W):
            if arows[h][w] == 'S':
                start = [h, w]
            elif arows[h][w] == 'T':
                end = [h, w]
    hs = [1, 0, -1, 0]
    ws = [0, -1, 0, 1]

    ne_eg = [[0] * W for _ in range(H)]
    queue = deque()
    queue.append((end, 0))
    visited = [[False] * W for _ in range(H)]
    while queue:
        now, e = queue.popleft()
        visited[now[0]][now[1]] = True
        ne_eg[now[0]][now[1]] = e
        # 行ける場所探し
        for h_s, w_s in zip(hs, ws):
            nh = now[0] + h_s
            nw = now[1] + w_s
            if nh >= H or nh < 0:
                continue
            if nw >= W or nw < 0:
                continue
            if arows[nh][nw] == '#':
                continue
            if visited[nh][nw]:
                continue
            queue.append(([nh, nw], e + 1))

    queue = deque()
    # 管理するのは、index, 現状のエネルギー
    queue.append((start, 0))

    while queue:
        now, e = queue.popleft()
        # エネルギーが0?
        if es.get(f'{now[0]}{now[1]}', 0) > e:
            e = es.get(f'{now[0]}{now[1]}')
            es[f'{now[0]}{now[1]}'] = 0
        if e == 0:
            continue

        if e >= ne_eg[now[0]][now[1]]:
            print('Yes')
            return

        # 行ける場所探し
        for h_s, w_s in zip(hs, ws):
            nh = now[0] + h_s
            nw = now[1] + w_s
            if nh >= H or nh < 0:
                continue
            if nw >= W or nw < 0:
                continue
            if arows[nh][nw] == '#':
                continue
            queue.append(([nh, nw], e - 1))

    print('No')

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
