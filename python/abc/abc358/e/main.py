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
MOD = 998244353
num_list = []
str_list = []
import ast

@cache
def recursive(deep, C26):

    C26 = ast.literal_eval(C26)
    if deep == 1:
        return 26 - C26.count(False)

    count = 0
    for i, c in enumerate(C26):
        if not c:
            continue
        c_c26 = deepcopy(C26)
        c_c26[i] -= 1
        for ci, c in enumerate(c_c26):
            if deep < c:
                c_c26[ci] = deep
        count += recursive(deep - 1, str(c_c26))
        count %= MOD

    return count

def main():
    K = i_input()
    C26 = i_list()

    result = 0
    '''
    考えたいこと、Kが1増えたときに、どれくらい増えるのか
    K = 1
    0 or 1

    K = 2
    AA等Cが2↑の場合に増える
    A? or ?A

    K = 3
    A?? or ?A? or ??A or AA? or A?A or ?AA

    これ再帰で行けね?'
    A?と?って状態的に言えば同じなわけで、?としてあり得る値が来るだけ
    A??と??も同じ。??からB?になっても同じ
    '''

    for i in range(1, K + 1):
        c_c26 = deepcopy(C26)
        for ci, c in enumerate(c_c26):
            if i < c:
                c_c26[ci] = i
        result += recursive(i, str(c_c26))
        result %= MOD

    print(result % MOD)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
