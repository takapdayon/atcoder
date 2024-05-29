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

def can_win(cards):
    # 次勝てるか
    count = 0
    count2 =0
    comb = set()
    comb2 = set()
    for a in range(len(cards) - 1):
        for b in range(a, len(cards)):
            if cards[a][0] == cards[b][0] and a not in comb and b not in comb:
                comb.add(a)
                comb.add(b)
                count += 1

    for a in range(len(cards) - 1):
        for b in range(a, len(cards)):
            if cards[a][1] == cards[b][1] and a not in comb and b not in comb:
                comb2.add(a)
                comb2.add(b)
                count2 += 1

    return min(count, count2) == 1

import copy

def get_nexts(cards):
    # 次消すパターンを返す
    patterns = []
    for a in range(len(cards) - 1):
        for b in range(a, len(cards)):
            if cards[a][0] == cards[b][0]:
                new_c = copy.deepcopy(cards)
                patterns.append(
                    new_c[:a]+new_c[a:b]+new_c[b:]
                )

    for a in range(len(cards) - 1):
        for b in range(a, len(cards)):
            if cards[a][1] == cards[b][1]:
                new_c = copy.deepcopy(cards)
                patterns.append(
                    new_c[:a-1]+new_c[a:b-1]+new_c[b:]
                )

    return patterns

def dfs(cards, player):
    # 次勝てる盤面があるか
    if can_win(cards):
        return player

    # 勝てないなら一枚消す先を全部次のプレイヤーに渡す
    next_do = get_nexts(cards)
    for next in next_do:
        if can_win(next):
            return player
        if not dfs(next, not player):
            return player
        return not player

def main():
    N = i_input()
    ABs = i_row_list(N)

    res = dfs(ABs, 1)
    if res == 1:
        print("Takahashi")
    else:
        print("Aoki")


if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
