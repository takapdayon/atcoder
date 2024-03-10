import sys, re
import random
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial, atan, degrees, exp
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

def dist(x1, y1, x2, y2):
    return sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

def get_score(n, xyrows, c):
    score = 0
    for i in range(n - 1):
        score += dist(xyrows[c[i]][0], xyrows[c[i]][1], xyrows[c[i + 1]][0], xyrows[c[i + 1]][1])
    score += dist(xyrows[c[0]][0], xyrows[c[0]][1], xyrows[c[-1]][0], xyrows[c[-1]][1])
    return score

def greedy(n, xyrows):
    visited = [False] * n
    visited[0] = True
    ans = [0]
    pos = 0

    for _ in range(n):
        min = 10 ** 9
        to = -1
        for i in range(n):
            if visited[i]:
                continue
            if dist(xyrows[pos][0], xyrows[pos][1], xyrows[i][0], xyrows[i][1]) < min:
                min = dist(xyrows[pos][0], xyrows[pos][1], xyrows[i][0], xyrows[i][1])
                to = i
        if to != -1:
            visited[to] = True
            ans.append(to)
            pos = to
    ans.append(0)
    # for a in ans:
    #     print(a)
    return ans

def local_search(n, xyrows):
    # そもそもの初期配列も何度か試そう
    time_keeper = TimeKeeper(950)
    ans = [ i % n for i in range(n + 1)]
    score = get_score(n, xyrows, ans)
    while not time_keeper.is_time_over():
        le = random.randint(1, n - 1)
        ri = random.randint(le, n - 1)
        ans[le:ri + 1] = reversed(ans[le:ri + 1])
        if score > get_score(n, xyrows, ans):
            score = get_score(n, xyrows, ans)
        else:
            ans[le:ri + 1] = reversed(ans[le:ri + 1])

    for a in ans:
        print(a + 1)

class TimeKeeper:
    def __init__(self, time_threshold) -> None:
        self.time_threshold = time_threshold
        self.start_time = time.time()
        self.before_time = self.start_time

    def now_time(self):
        return time.time()

    def set_time(self):
        self.before_time = time.time()

    def is_time_over(self):
        now = time.time()
        diff = now - self.start_time
        return (diff * 1000) >= self.time_threshold

class TempManager:
    def __init__(self, start_temp = 50, end_temp = 10) -> None:
        self.start_temp = start_temp
        self.end_temp = end_temp

    def temp(self, tk):
        return self.start_temp + (self.end_temp - self.start_temp) * ((tk.now_time() - tk.start_time) * 1000) / tk.time_threshold

    def probability(self, new, pre, temp):
        return exp((new - pre) / temp)

    def should_change(self, probability):
        return random.random() < probability

def sa(n, xyrows):
    time_keeper = TimeKeeper(950)
    # 適用する温度?この範囲でジャンプする
    temp_manager = TempManager(30, 2)

    # ans = [ i % n for i in range(n + 1)]
    ans = greedy(n, xyrows)
    score = get_score(n, xyrows, ans)

    while not time_keeper.is_time_over():
        le = random.randint(1, n - 1)
        ri = random.randint(le, n - 1)
        ans[le:ri + 1] = reversed(ans[le:ri + 1])

        new_score = get_score(n, xyrows, ans)

        temp = temp_manager.temp(time_keeper)
        probability = temp_manager.probability(-new_score, -score, temp)

        if temp_manager.should_change(probability):
            score = new_score
        else:
            ans[le:ri + 1] = reversed(ans[le:ri + 1])

    for a in ans:
        print(a + 1)

def main():
    n = i_input()
    xyrows = i_row_list(n)
    sa(n, xyrows)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
