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
NEXT = list(zip([1, 0, -1, 0], [0, -1, 0, 1]))

def main():
    H, W = i_map()
    SH = s_row_list(H)
    A, B, C, D = i_map()

    memo = [[1000000] * W for _ in range(H)]
    memo[A - 1][B - 1] = 0
    queue = deque([(A - 1, B - 1)])

    while queue:
        a, b = queue.popleft()
        for i in range(1, 3):
            for nhi, nwi in NEXT:
                nhi, nwi = nhi * i, nwi * i
                nh, nw = nhi + a, nwi + b
                if nh < 0 or nw < 0 or nh >= H or nw >= W:
                    continue

                # if memo[nh][nw] != -1:
                #     continue

                if SH[nh][nw] != '#':
                    if i == 1 and memo[nh][nw] > memo[a][b]:
                        memo[nh][nw] = memo[a][b]
                        queue.appendleft((nh, nw))
                else:
                    if memo[nh][nw] > memo[a][b] + 1:
                        memo[nh][nw] = memo[a][b] + 1
                        queue.appendleft((nh, nw))


    print(memo[C - 1][D - 1])

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055

