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

class TimeKeeper:
    def __init__(self, N) -> None:
        self.time_threshold = 4 * (N ** 2)

        self.start_time = 0
        self.before_time = 0

    def now_time(self):
        return self.before_time

    def set_time(self):
        # 必要であれば、進めた情報をここで更新する
        self.before_time += 1

    def is_time_over(self):
        # 思考タイムが残っているか
        now = time.time()
        whole_diff = now - self.start_time
        whole_count = int(whole_diff * 1000)

        return whole_count >= self.time_threshold

class TempManager:
    def __init__(self, start_temp = 50, end_temp = 10) -> None:
        self.start_temp = start_temp
        self.end_temp = end_temp

    def temp(self, tk):
        return self.start_temp + (self.end_temp - self.start_temp) * ((tk.now_time() - tk.start_time) * 1000) / tk.time_threshold

    def probability(self, new, pre, temp):
        return math.exp((new - pre) / temp)

    def should_change(self, probability):
        return random.random() < probability

class Player:
    def __init__(self) -> None:
        pass

class State:
    def __init__(self, N, w_walls, h_walls, values) -> None:
        self.N = N
        self.w_walls = w_walls
        self.h_walls = h_walls
        self.values = values
        self.p1 = [N // 2, N // 2]
        self.p2 = [N // 2, N // 2]
        if self.N % 2 == 0:
            self.p2[0] += 1
            self.p2[1] += 1

        self.visited = {}

        self.ini_pos()

    def ini_pos(self):
        print(f'{self.p1[0]} {self.p1[1]} {self.p2[0]} {self.p2[1]}')

    def reset_visit(self):
        self.visited = {}

    @classmethod
    def copy(cls):
        '''遷移関数'''
        pass

    def get_score(self):
        # スコアすべてを返す
        score = 0
        return score

    def get_part_score(self, h, w):
        # 一部のスコアを返す
        score = 0
        hl = [1, 0, -1, 0]
        wl = [0, -1, 0, 1]

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
            score += abs(self.values[h][w] - self.values[h + nh][w + nw])

        return score

    def next_action(self):
        next_actions = self._move_to()

        if not next_actions:
            self.visited = self.reset_visit()
            next_actions = self._move_to()

        score = [ 10 ** 10, [], []]
        for n_p1, n_p2 in next_actions:
            self.values[n_p1[0]][n_p1[1]], self.values[n_p2[0]][n_p2[1]] = self.values[n_p2[0]][n_p2[1]], self.values[n_p1[0]][n_p1[1]]
            # スワップした後のスコアを計算
            # 差し引いて最大の成果を得られるなら移動
            p1_s = self.get_part_score(n_p1[0], n_p1[1])
            p2_s = self.get_part_score(n_p2[0], n_p2[1])
            if p1_s + p2_s < score[0]:
                score[0] = p1_s + p2_s
                score[1] = n_p1
                score[2] = n_p2
            self.values[n_p1[0]][n_p1[1]], self.values[n_p2[0]][n_p2[1]] = self.values[n_p2[0]][n_p2[1]], self.values[n_p1[0]][n_p1[1]]

        p1_m = self.conv_action(score[1][0] - self.p1[0], score[1][1] - self.p1[1])
        p2_m = self.conv_action(score[2][0] - self.p2[0], score[2][1] - self.p2[1])
        print(f'1 {p1_m} {p2_m}')

        # 動いた後に更新
        self.update(score[1], score[2])

    def update(self, p1, p2):
        # 値の更新処理
        self.p1 = p1
        self.p2 = p2
        self.values[self.p1[0]][self.p1[1]], self.values[self.p2[0]][self.p2[1]] = self.values[self.p2[0]][self.p2[1]], self.values[self.p1[0]][self.p1[1]]
        self.p1_visited[self.p1[0]][self.p1[1]] = True
        self.p2_visited[self.p2[0]][self.p2[1]] = True

    def conv_action(self, h, w):
        if h == 1:
            return 'U'
        elif h == -1:
            return 'D'
        elif w == 1:
            return 'R'
        elif w == -1:
            return 'L'
        else:
            return '.'

    def _move_to(self):
        # playerの1手先行動できるものを返す
        hl = [1, 0, -1, 0, 0]
        wl = [0, -1, 0, 1, 0]
        p1_nas = []
        p2_nas = []
        move_to = []

        for nh, nw in zip(hl, wl):
            # 差分スコアを足す
            if self._can_move(self.p1[0], self.p1[1], nh, nw):
                p1_nas.append([self.p1[0] + nh, self.p1[1] + nw])
            if self._can_move(self.p2[0], self.p2[1], nh, nw):
                p1_nas.append([self.p2[0] + nh, self.p2[0] + nw])

        for p1_na in p1_nas:
            for p2_na in p2_nas:
                self.values[p1_na[0]][p1_na[1]], self.values[p2_na[0]][p2_na[1]] = self.values[p2_na[0]][p2_na[1]], self.values[p1_na[0]][p1_na[1]]
                if self.visited.get(str(self.values), False):
                    continue
                else:
                    move_to[[p1_na, p2_na]]
                self.values[p1_na[0]][p1_na[1]], self.values[p2_na[0]][p2_na[1]] = self.values[p2_na[0]][p2_na[1]], self.values[p1_na[0]][p1_na[1]]

        return move_to

    def _can_move(self, h, w, nh, nw):
        # 端であればcontinue
        if h + nh == self.N or h + nh == -1:
            return False
        if w + nw == self.N or w + nw == -1:
            return False
        # 壁があればcontinue
        if nh == 1 and self.h_walls[h][w] == '1':
            return False
        if nh == -1 and self.h_walls[h - 1][w] == '1':
            return False
        if nw == 1 and self.w_walls[h][w] == '1':
            return False
        if nw == -1 and self.w_walls[h][w - 1] == '1':
            return False
        return True

def main():
    t, N = i_map()
    w_walls = s_row_list(N)
    h_walls = s_row_list(N - 1)
    values = i_row_list(N)

    state = State(N, w_walls, h_walls, values)

    for i in range(2 * (N ** 2) - 5):
        state.next_action()

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
