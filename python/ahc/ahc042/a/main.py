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

ACTIONS = ["L", "R", "U", "D"]

class ManageGrid:
    def __init__(self, CN, N):
        self.N = N
        self.CN = CN
        self.count = self._initial_oni()
        self.results = []

    def _initial_oni(self):
        count = 0
        for h in range(self.N):
            for w in range(self.N):
                if self.CN[h][w] == 'x':
                    count += 1
        return count

    def check_huku(self, act, h, w):
        if act == "L":
            for l in range(w):
                if self.CN[h][l] == 'o':
                    return False
            return True

        if act == "R":
            for r in range(w, self.N):
                if self.CN[h][r] == 'o':
                    return False
            return True

        if act == "U":
            for u in range(h):
                if self.CN[u][w] == 'o':
                    return False
            return True
        if act == "D":
            for d in range(h, self.N):
                if self.CN[d][w] == 'o':
                    return False
            return True

    def move(self, act, h, w):
        if act == "L":
            for _ in range(w + 1):
                self.move_grid(act, h)
        if act == "R":
            for r in range(w, self.N):
                self.move_grid(act, h)
        if act == "U":
            for u in range(h + 1):
                self.move_grid(act, w)
        if act == "D":
            for d in range(h, self.N):
                self.move_grid(act, w)

    def move_grid(self, act, num):
        if act == "L":
            if self.CN[num][0] == 'x':
                self.count -= 1
            self.CN[num].pop(0)
            self.CN[num].append('.')
            self.results.append(["L", num])
        elif act == "R":
            if self.CN[num][self.N - 1] == 'x':
                self.count -= 1
            self.CN[num].pop()
            self.CN[num].insert(0, '.')
            self.results.append(["R", num])
        elif act == "U":
            if self.CN[0][num] == 'x':
                self.count -= 1
            for h in range(self.N - 1):
                self.CN[h][num] = self.CN[h + 1][num]
            self.CN[self.N - 1][num] = '.'
            self.results.append(["U", num])
        elif act == "D":
            if self.CN[self.N - 1][num] == 'x':
                self.count -= 1
            for h in reversed(range(1, self.N)):
                self.CN[h][num] = self.CN[h - 1][num]
            self.CN[0][num] = '.'
            self.results.append(["D", num])

def main():
    N = i_input()
    CN = s_row_list(N)
    manager = ManageGrid(CN, N)

    while manager.count:
        for h in range(N):
            for w in range(N):
                if manager.CN[h][w] != 'x':
                    continue
                for act in ACTIONS:
                    val = manager.check_huku(act, h, w)
                    if val:
                        manager.move(act, h, w)

    for result in manager.results:
        print(*result)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
