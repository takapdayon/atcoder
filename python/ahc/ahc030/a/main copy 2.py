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

class Polyomino:

    def __init__(self, size, shape) -> None:
        self.size = size
        self.shape = shape

    def search_polyomino(self, N, M, oil, has_o):
        for i in range(N):
            for j in range(N):
                pass
        return oil, has_o

def ans1(N, M, eps, polyominos):

    oil = [[0] * N for _ in range(N)]
    has_o = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if (i + j) % 2:
                continue
            print("q 1 {} {}".format(i, j))
            resp = input()
            if resp != "0":
                oil[i][j] == int(resp)
                has_o[i][j] == True

    polyominos = sorted(polyominos, key=lambda p: p.size, reverse=True)

    for i in range(N):
        for j in range(N):
            if has_o[i][j]:
                for polyomino in polyominos:
                    oil, has_o = polyomino.search(N, M, oil, has_o)

    ans = []
    for i in range(N):
        for j in range(N):
            if has_o[i][j]:
                ans.append((i, j))

    print("a {} {}".format(len(ans), ' '.join(map(lambda x: "{} {}".format(x[0], x[1]), ans))))
    resp = input()
    assert resp == "1"

def main():
    line = input().split()
    N = int(line[0])
    M = int(line[1])
    eps = float(line[2])
    polyominos = []
    for _ in range(M):
        line = input().split()
        ps = []
        for i in range(int(line[0])):
            ps.append((int(line[2*i+1]), int(line[2*i+2])))
        polyominos.append(Polyomino(line[0], ps))

    ans1(N, M, eps, polyominos)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
