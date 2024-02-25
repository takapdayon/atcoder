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

    def __init__(self) -> None:
        pass

    def count(self):
        '''総ポリゴン数はいくつか'''
        pass

    def h_size(self):
        '''このテトリスを収めるのに縦何マス必要か'''
        pass

    def w_max_size(self):
        '''このテトリスを収めるのに横何マス必要か'''
        pass

    def can_include(self, h, w):
        '''h, wの長さの部分は存在するか'''
        pass

class ManagePolyominos:

    def __init__(self) -> None:
        pass


def ans1(N, M, eps):
    '''
    上下左右で分割し、存在するならnを2になるまで分割。2以下になった時点で1orderで求める
    '''
    ans = SortedSet()
    oil = [[False] * (N + 2) for _ in range(N + 2)]
    checked = [[False] * (N + 2) for _ in range(N + 2)]
    for h in range(0, N - 1, 2):
        for w in range(0, N - 1, 2):
            q = [(h, w), (h + 1, w), (h, w + 1), (h + 1, w + 1)]
            if w + 3 == N:
                q.extend([(h, w + 2), (h + 1, w + 2)])
            if h + 3 == N:
                q.extend([(h + 2, w), (h + 2, w + 1)])
            if h + 3 == N and w + 3 == N:
                q.extend([(h + 2, w + 2)])
            unp = [item for subl in q for item in subl]
            print(f"q {len(q)} {' '.join(map(str, unp))}")
            resp = input()
            if resp != "0":
                for i in q:
                    print(f"q 1 {i[0]} {i[1]}")
                    resp2 = input()
                    checked[i[0] + 1][i[1] + 1] = True
                    if resp2 != "0":
                        oil[i[0] + 1][i[1] + 1] = True
                        ans.add(i)


    print("a {} {}".format(len(ans), ' '.join(map(lambda x: "{} {}".format(x[0], x[1]), ans))))
    resp = input()

    while resp == '0':
        oil_c = oil.copy()
        for h in range(1, N + 1):
            for w in range(1, N + 1):
                if checked[h][w]:
                    continue
                if any([oil[h - 1][w - 1], oil[h - 1][w], oil[h - 1][w + 1], oil[h][w - 1], oil[h][w + 1], oil[h + 1][w - 1], oil[h + 1][w], oil[h + 1][w + 1]]):
                    print(f"q 1 {h - 1} {w - 1}")
                    resp2 = input()
                    checked[h][w] = True
                    if resp2 != "0":
                        oil_c[h][w] = True
                        ans.add((h - 1, w - 1))
        oil = oil_c
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
        polyominos.append(ps)

    ans1(N, M, eps)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
