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

N = 50
U = 0
D = 1
L = 2
R = 3
ACTIONS = [U, D, L, R]
ACTION_CHAR = 'UDLR'

TO_H = [-1, 1, 0, 0]
TO_W = [0, 0, -1, 1]

import time

class TimeKeeper:
    def __init__(self, time_threshold) -> None:
        self.time_threshold = time_threshold
        self.start_time = time.time()
        self.before_time = self.start_time

    def set_time(self):
        self.before_time = time.time()

    def is_time_over(self):
        # 思考タイムが残っているか
        now = time.time()
        whole_diff = (now * 1000) - (self.start_time * 1000)
        return whole_diff >= self.time_threshold

def dfs(pos, visited, points, pairs):
    '''
    自分から先に行ける方向に向かっていった際に、最大値となる方向をreturnする
    '''
    visited[pairs[pos[0]][pos[1]]] = True
    to_list = []

    for i, (h, w) in enumerate(zip(TO_H, TO_W)):
        # 超えないように弾く
        if pos[0] + h == N or pos[0] + h < 0 or pos[1] + w == N or pos[1] + w < 0:
            continue
        # 訪問済みはスルー
        if visited[pairs[pos[0] + h][pos[1] + w]]:
            continue
        to_list.append((i, (pos[0] + h, pos[1] + w)))

    if not to_list:
        return '', points[pos[0]][pos[1]]

    max_point = 0
    paths = ''

    for di, to in to_list:
        # どの方向に進んだかと、そのポイントがいくつだったかをメモ
        # 最大値の経路と点数を追加して返す
        path, point = dfs(to, visited, points, pairs)
        if point > max_point:
            max_point = point
            paths = ACTION_CHAR[di] + path
    return paths, max_point + points[pos[0]][pos[1]]

def local_search(paths):
    '''
    遷移条件を満たす形でローカルサーチを行う
    単純なランダムにするローカルサーチだと遷移条件を満たさない可能性があるため、大近傍探索法にする
    '''

def main():
    si, sj = i_map()
    pairs = i_row_list(N)
    points = i_row_list(N)

    time_keeper = TimeKeeper
    visited = [False] * (N ** 2 - 1)

    paths, score = dfs((si, sj), visited, points, pairs)
    while time_keeper.is_time_over():
        # 時間切れになるまでlocal searchをする
        new_paths, new_score = local_search()
        if score < new_score:
            paths = new_paths
            score = new_score

    print(paths)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
