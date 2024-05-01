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

def main():
    H, W = i_map()
    start = i_list()
    goal = i_list()
    matrix = s_row_list(H)
    '''
    ダイクストラで重みをもっていればいいかな。
    重みの判定だけめんどくて、前回の値を保持していないといけないのか...?
    '''
    queue = []
    queue.append((-1, (start[0] - 1, start[1] - 1), None))
    dist = [INF] * (H * W + 1)
    cnf = [False] * (H * W + 1)
    dist[(start[0] - 1) * W + start[1] - 1] = 0

    while queue:
        d, now, dire = heappop(queue)
        cnf[now[0] * W + now[1]] = True
        for nhi, nwi in zip([1, 0, -1, 0], [0, -1, 0, 1]):
            nh, nw = now[0] + nhi, now[1] + nwi
            if nh < 0 or nw < 0 or nh >= H or nw >= W:
                continue
            if matrix[nh][nw] == '#':
                continue
            if cnf[nh * W + nw]:
                continue
            cost = d
            if dire != (nhi, nwi):
                cost += 1
            if cost < dist[nh * W + nw]:
                dist[nh * W + nw] = cost
                heappush(queue, (cost, (nh, nw), (nhi, nwi)))

    print(dist[(goal[0] - 1) * W + goal[1] - 1])

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
