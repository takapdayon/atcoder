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

def main():
    t, N = i_map()
    w_walls = s_row_list(N)
    h_walls = s_row_list(N - 1)
    values = i_row_list(N)

    for i in range(2 * (N ** 2) - 5):
        state.next_action()

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
