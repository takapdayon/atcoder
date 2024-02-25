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
def s_row_list(N): return [s_list() for _ in range(N)]

sys.setrecursionlimit(10 ** 6)

INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

H = 10
W = 10
TURN = 100
F = 0
B = 1
L = 2
R = 3
ACTIONS = [F, B, L, R]
ACTION_CHAR = 'FBLR'

import time
import random

mt = random.Random(0)  # シード0でメルセンヌツイスターの乱数生成器を初期化

class TimeKeeper:
    def __init__(self, time_threshold) -> None:
        self.time_threshold = time_threshold
        self.turn = 0

        self.start_time = time.time()
        self.before_time = self.start_time

    def set_turn(self, turn):
        # 今が何ターン目かを受け取る
        self.turn = turn
        self.before_time = time.time()

    def is_time_over(self):
        now = time.time()
        whole_diff = now - self.start_time
        whole_count = int(whole_diff * 1000)
        last_diff = now - self.before_time
        last_count = int(last_diff * 1000)

        remaining_time = self.time_threshold - whole_count
        now_threshold = remaining_time / (TURN - self.turn)
        return last_count >= now_threshold

class State:
    def __init__(self, candies) -> None:
        self.t = 0
        self.board = [[0] * W for _ in range(H)]
        self.candies = candies

    @classmethod
    def copy(cls, source):
        instance = cls(source.candies)
        instance.board = [row[:] for row in source.board]
        instance.t = source.t
        return instance

    def is_done(self):
        return self.t >= TURN

    def advance(self, action):
        # キャンディを一つ進める
        if action == F:
            for x in range(W):
                dest = 0
                for y in range(dest, H):
                    if self.board[y][x] != 0:
                        self.board[dest][x], self.board[y][x] = self.board[y][x], self.board[dest][x]
                        dest += 1
        elif action == B:
            for x in range(W):
                dest = H - 1
                for y in range(dest, -1, -1):
                    if self.board[y][x] != 0:
                        self.board[dest][x], self.board[y][x] = self.board[y][x], self.board[dest][x]
                        dest -= 1
        elif action == L:
            for y in range(H):
                dest = 0
                for x in range(dest, W):
                    if self.board[y][x] != 0:
                        self.board[y][dest], self.board[y][x] = self.board[y][x], self.board[y][dest]
                        dest += 1
        elif action == R:
            for y in range(H):
                dest = W - 1
                for x in range(dest, -1, -1):
                    if self.board[y][x] != 0:
                        self.board[y][dest], self.board[y][x] = self.board[y][x], self.board[y][dest]
                        dest -= 1
        self.t += 1

    def random_update(self):
        reverse_t = TURN - self.t
        if reverse_t == 0:
            return
        p = mt.randint(1, reverse_t)
        pos = 0
        for h in range(H):
            for w in range(W):
                if self.board[h][w] == 0:
                    p -= 1
                if p == 0:
                    pos = h * 10 + w
                    break
        self.update(pos)

    def update(self, pt):
        h = pt // W
        w = pt % W
        self.board[h][w] = self.candies[self.t]

    def get_score(self):
        score = 0
        checked = [[0] * W for _ in range(H)]
        for h in range(H):
            for w in range(W):
                if self.board[h][w] != 0 and not checked[h][w]:
                    group_size = self._get_group_size(h, w, checked)
                    score += group_size * group_size
        return score

    def _get_group_size(self, h, w, checked):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        candy = self.board[h][w]
        checked[h][w] = True

        q = deque([(h, w)])
        cnt = 0
        while q:
            cnt += 1
            now_y, now_x = q.popleft()
            for di in range(4):
                ty = now_y + dy[di]
                tx = now_x + dx[di]
                if 0 <= ty < H and 0 <= tx < W and not checked[ty][tx] and self.board[ty][tx] == candy:
                    checked[ty][tx] = True
                    q.append((ty, tx))
        return cnt

def play_1turn(state):
    if state.candies[state.t] == 1:
        return ACTIONS[0]
    if state.candies[state.t] == 2:
        return ACTIONS[1]
    return ACTIONS[2]

def playout(state):
    state.advance(play_1turn(state))
    while not state.is_done():
        state.random_update()
        state.advance(play_1turn(state))
    return state.get_score()

def primitive_montecalro(time_keeper, base_state):
    w = [0] * len(ACTIONS)

    '''
    まずは回数分だけ回すようにする
    '''
    while True:
        if time_keeper.is_time_over():
            break
        for d in ACTIONS:
            state = State.copy(base_state)
            state.advance(d)
            state.random_update()
            if state.is_done():
                w[d] += state.get_score()
            else:
                w[d] += playout(state)

    ret = -1
    best = -1
    for d in range(len(ACTIONS)):
        if w[d] > best:
            ret = d
            best = w[d]
    return ret

def main():
    candies = i_list()
    time_keeper = TimeKeeper(1750)
    state = State(candies)

    for t in range(TURN):
        time_keeper.set_turn(t)
        pos = i_input()
        state.update(pos)
        action = primitive_montecalro(time_keeper, state)
        print(ACTION_CHAR[action])
        state.advance(action)

    return 0

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
