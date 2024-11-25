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

from atcoder.dsu import DSU

def main():
    N, Q = i_map()
    uf = DSU(N + 1)
    memo = defaultdict(int)
    for i in range(N + 1):
        memo[i] = 1

    color = defaultdict{int}
    for i in range(1, N + 1):
        color[i] = i

    for q in range(Q):
        query = i_list()
        if query[0] == 2:
            print(memo[query[1]])
            continue
        # query1

        if query[1] == 1:
            if query[1] + 1 == query[2]:
                pass

        color[uf.leader(query[1])] = query[2]
        memo[color(uf.leader(query[1]))] -= 1
        memo[query[2]] += uf.size(query[1])

        # if query[1] == 1:
        #     if uf.same(1, 2):
        #         memo[color[uf.leader(1)]] -= uf.leader(1)
        #         color[uf.leader(1)] = query[2]
        #         memo[query[2]] += uf.leader(1)
        #     else:
        #         if query[2] == 2:
        #             color[1] = 2
        #             memo[1] -= 1
        #             memo[color[uf.leader(1)]] -= uf.leader(1)
        #             color[uf.leader(1)] = query[2]

        #             memo[1] -= 1
        #             memo[uf.leader(2)] -= uf.size(2)
        #             uf.merge(1, 2)
        #             memo[uf.leader(1)] += uf.size(1)
        #         else:
        #             memo[1] -= 1
        #             memo[uf.leader(query[2])] += 1

        # elif query[1] == N:
        #     if uf.same(N, N - 1):
        #         memo[uf.leader(N)] -= uf.leader(N)
        #         memo[uf.leader(query[2])] += uf.leader(N)
        #     else:
        #         if query[2] == N - 1:
        #             memo[N] -= 1
        #             memo[uf.leader(N - 1)] -= uf.size(N - 1)
        #             uf.merge(N, N - 1)
        #             memo[uf.leader(N)] += uf.size(N)
        #         else:
        #             memo[N] -= 1
        #             memo[uf.leader(query[2])] += 1

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
