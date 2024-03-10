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

import time
import random
import math
random.seed(1)

N = 30  # タイルの長さ

T0 = 0
T1 = 1
T2 = 2
T3 = 3
T4 = 4
T5 = 5
T6 = 6
T7 = 7
TAIL_TYPE = [T0, T1, T2, T3, T4, T5, T6, T7]

TR0 = 0
TR1 = 1
TR2 = 2
TR3 = 3
ACTION_TYPE = [TR0, TR1, TR2, TR3] # 回転タイプ


class TimeKeeper:
    def __init__(self, time_threshold) -> None:
        self.time_threshold = time_threshold

        self.start_time = time.time()
        self.before_time = self.start_time

    def now_time(self):
        return time.time()

    def set_time(self):
        # 必要であれば、進めた情報をここで更新する
        self.before_time = time.time()

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

class State:


def main():
    tails = [list(map(int, list(s_input()))) for _ in range(N)]
    turns = [[0] * N for _ in range(N)]

    time_keeper = TimeKeeper(1800)
    tm = TempManager()

    state = State()

    while time_keeper.is_time_over():
        '''
        時間になるまでturnsの値を変える
        '''

    ans = ''
    for turn in turns:
        for c in turn:
            ans += str(c)
    print(ans)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
