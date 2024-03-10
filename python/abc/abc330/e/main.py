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

def main():
    n, q = i_map()
    alist = i_list()
    alist = [a + 1  for a in alist]
    exist = SortedSet()
    n_exist = SortedSet()
    count = defaultdict(int)
    for a in alist:
        exist.add(a)
        count[a] += 1

    for i in range(1, n + 2):
        if i in exist:
            continue
        n_exist.add(i)

    for i in range(q):
        i, x = i_map()
        x += 1

        pre = alist[i  - 1]
        alist[i - 1] = x
        count[pre] -= 1
        count[x] += 1
        if count[pre] == 0:
            exist.discard(pre)
            n_exist.add(pre)
        if count[x] == 1:
            n_exist.discard(x)
            exist.add(x)
        print(n_exist[0] - 1)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
