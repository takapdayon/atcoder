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
    Q = i_input()
    queries = i_row_list(Q)
    queue = deque()
    height = [0] * (Q + 1)

    for q in range(Q):
        if queries[q][0] == 1:
            height[q + 1] = height[q]
            queue.append(q)
        if queries[q][0] == 2:
            height[q + 1] = height[q] + queries[q][1]
            continue
        if queries[q][0] == 3:
            height[q + 1] = height[q]
            count = 0
            while queue:
                if height[q + 1] - height[queue[0]] >= queries[q][1]:
                    count += 1
                    queue.popleft()
                else:
                    break

            print(count)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
