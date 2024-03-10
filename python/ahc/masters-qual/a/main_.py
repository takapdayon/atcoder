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

'''MEMO:
やりたいこと:

制限:
行動回数: 4N**2(N100で大体40000)

初期位置決めて、交換できるし移動できる
一番コストが少ないのは

ソート

'''

import time
import random
import math

U = 0
D = 1
L = 2
R = 3
S = 4
M_ACTIONS = [U, D, L, R, S]
M_ACTIONS_CHAR = 'UDLR.'

N_SWAP = 0
SWAP = 1
S_ACTIONS = [N_SWAP, SWAP]
S_ACTIONS_CHAR = '01'

class PlayerState:
    def __init__(self, N, ) -> None:
        self.N = N
        self.p1 = [0, 0]
        self.p2 = [self.N - 1, self.N - 1]
        self.visited = {}

    def next_move(self):
        # playerの1手先行動できるものを返す
        hl = [1, 0, -1, 0, 0]
        wl = [0, -1, 0, 1, 0]
        next_action = []

        for nh, nw in zip(hl, wl):
            # 端であればcontinue
            if h + nh == self.N or h + nh == -1:
                continue
            if w + nw == self.N or w + nw == -1:
                continue
            # 壁があればcontinue
            if nh == 1 and self.h_walls[h][w] == '1':
                continue
            if nh == -1 and self.h_walls[h - 1][w] == '1':
                continue
            if nw == 1 and self.w_walls[h][w] == '1':
                continue
            if nw == -1 and self.w_walls[h][w - 1] == '1':
                continue
            # 差分スコアを足す
            if not visited[h + nh][w + nw]:
                next_action.append([h + nh, w + nw])

        return next_action

class SquareState:
    def __init__(self) -> None:
        pass



def main():
    t, N = i_map()
    w_walls = s_row_list(N)
    h_walls = s_row_list(N - 1)
    values = i_row_list(N)

    state = State(N, w_walls, h_walls, values)

    for i in range(4 * (N ** 2) - 10):
        state.next_action()

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
