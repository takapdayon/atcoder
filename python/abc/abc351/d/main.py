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

from atcoder.dsu import DSU

def judge(matrix, h, w, H, W):
    is_ok = True
    for nhi, nwi in zip([1, 0, -1, 0], [0, -1, 0, 1]):
        nh, nw = h + nhi, w + nwi
        if nh < 0 or nw < 0 or nh >= H or nw >= W:
            continue
        if matrix[nh][nw] == '#':
            is_ok = False
    return is_ok

def main():
    H, W = i_map()
    matrix = s_row_list(H)
    uf = DSU(H * W + 1)
    ss = []
    can_move = {}

    for h in range(H):
        for w in range(W):
            if matrix[h][w] == '#':
                continue
            if judge(matrix, h, w, H, W):
                can_move[(h * W + w)] = True
                # 右としたを見て、そいつらが遷移可能ならグループ化する
                for nhi, nwi in zip([0, 1], [1, 0]):
                    nh, nw = h + nhi, w + nwi
                    if nh >= H or nw >= W:
                        continue
                    if judge(matrix, nh, nw, H, W):
                        uf.merge((h * W + w), (nh * W + nw))
            else:
                ss.append((h, w))

    dd = defaultdict(int)
    for s in ss:
        done = {}
        for nhi, nwi in zip([1, 0, -1, 0], [0, -1, 0, 1]):
            nh, nw = s[0] + nhi, s[1] + nwi
            if nh < 0 or nw < 0 or nh >= H or nw >= W:
                continue
            if matrix[nh][nw] == '#':
                continue
            if done.get(uf.leader(nh * W + nw)):
                continue
            dd[uf.leader(nh * W + nw)] += 1
            done[uf.leader(nh * W + nw)] = True

    max_g = []
    for g in uf.groups():
        if len(g) == 1 and not can_move.get(g[0], False):
            continue
        if len(max_g) < len(g):
            max_g = g

    if len(max_g):
        if len(max_g) == 1:
            print(dd.get(uf.leader(max_g[0])))
        else:
            print(len(max_g) + dd.get(uf.leader(max_g[0])))
    else:
        print(1)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
