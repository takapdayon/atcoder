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
    N = i_input()
    Vn = i_list()
    odd_counter = Counter()
    even_counter = Counter()

    for i, v in enumerate(Vn):
        if i % 2:
            even_counter[v] += 1
        else:
            odd_counter[v] += 1

    result = 0

    # どっちも同じって特殊例
    if len(odd_counter) == 1 and len(even_counter) == 1 and odd_counter.keys() == even_counter.keys():
        print(odd_counter.total())
        return

    # どっちもそろえる数字が同じになってしまう場合は一つ妥協
    if odd_counter.most_common()[0][0] == even_counter.most_common()[0][0]:

        if odd_counter.most_common()[0][1] > even_counter.most_common()[0][1] or \
            (odd_counter.most_common()[0][1] == even_counter.most_common()[0][1] and odd_counter.most_common()[1][1] < even_counter.most_common()[1][1]):
            result += len(odd_counter) != 1 and odd_counter.total() - odd_counter.most_common()[0][1] or 0
            result += len(even_counter) != 1 and even_counter.total() - even_counter.most_common()[1][1] or 0
        else:
            result += len(odd_counter) != 1 and odd_counter.total() - odd_counter.most_common()[1][1] or 0
            result += len(even_counter) != 1 and even_counter.total() - even_counter.most_common()[0][1] or 0
        print(result)
        return

    result += len(odd_counter) != 1 and odd_counter.total() - odd_counter.most_common()[0][1] or 0
    result += len(even_counter) != 1 and even_counter.total() - even_counter.most_common()[0][1] or 0
    print(result)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
