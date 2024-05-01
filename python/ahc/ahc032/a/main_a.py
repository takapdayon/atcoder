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
MOD = 998244353
num_list = []
str_list = []

import time
import random
import math
mt = random.Random(0)

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
    def __init__(self, arows, stamp, k, n) -> None:
        self.arows = arows
        self.stamp = stamp
        self.m = len(self.stamp) - 1
        self.k = k
        self.n = n
        self.ans = [()] * self.k

    def copy(self):
        return State([a[:] for a in self.arows], self.stamp, self.k, self.n)

    def score(self):
        score = 0
        for arow in self.arows:
            for a in arow:
                score += a % MOD
        return score

    def do(self):
        '''
        状態遷移
        '''
        for t in range(self.k):
            # この時に一番よいスタンプを使う
            rs = mt.randint(0, self.m)
            rh = mt.randint(0, self.n - 3)
            rw = mt.randint(0, self.n - 3)
            for h in range(3):
                for w in range(3):
                    self.arows[h + rh][w + rw] += self.stamp[rs][h][w]
            self.ans[t] = (rs, rh, rw)

    def get_ans(self):
        return self.ans

def get_score(arows):
    score = 0
    for arow in arows:
        for a in arow:
            score += a % MOD
    return score

def main():
    N, M, K = i_map()
    arows = i_row_list(N)
    stamp = []
    for s in range(M):
        s1 = i_list()
        s2 = i_list()
        s3 = i_list()
        stamp.append((s1, s2, s3))

    ans = []

    for k in range(K):
        high_ans = ()
        h_score = get_score(arows)
        c_arows = [a[:] for a in arows]
        for si, s in enumerate(stamp):
            for h in range(N - 2):
                for w in range(N - 2):
                    t_rows = [a[:] for a in arows]
                    for ph in range(3):
                        for pw in range(3):
                            t_rows[h + ph][w + ph] += s[ph][pw]
                    if h_score < get_score(t_rows):
                        high_ans = (si, h, w)
                        h_score = get_score(t_rows)
                        c_arows = t_rows

        if high_ans:
            ans.append(high_ans)
            arows = c_arows

    print(len(ans))
    for a in ans:
        print(*a)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
