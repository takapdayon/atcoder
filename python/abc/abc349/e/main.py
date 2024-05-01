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

def hh(mas, Arows, turn):
    choice = []
    val = (10 ** 10) * -1
    for i in range(9):
        if mas[i // 3][i % 3] is not None:
            continue
        # Noneで選択できるなら選択肢に加える
        choice.append(i)

    for c in choice:
        c_mas = [i[:] for i in mas]
        c_mas[[c // 3][c % 3]] = turn
        val = max(val, Arows[c // 3][c % 3])

    return val

def main():
    Arows = i_row_list(3)
    mas = [[None] * 3 for _ in range(3)]
    takahashi = 0
    aoki = 0

    for i in range(9):
        turn = i % 2 == 0

        val = 0
        if turn:
            takahashi += val
        else:
            aoki += val

    print(takahashi > aoki and 'Takahashi' or 'Aoki')

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
