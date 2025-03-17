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
    S = list(s_input())
    ones = []
    for i, s in enumerate(S):
        if s == '1':
            ones.append(i)

    if len(ones) == 1:
        print(0)
        return
    if len(ones) == 2:
        print(abs(ones[0] - ones[1]) - 1)
        return

    count = 0

    mid = len(ones) // 2
    left = mid
    right = mid

    while left != 0 or right != len(ones) - 1:
        if left == 0:
            right += 1
            count += ones[right] - ones[mid] - (right - mid)
            continue
        if right == len(ones) - 1:
            left -= 1
            count += ones[mid] - ones[left] - (mid - left)
            continue
        else:
            if ones[mid] - ones[left - 1] > ones[right + 1] - ones[mid]:
                right += 1
                count += ones[right] - ones[mid] - (right - mid)
            else:
                left -= 1
                count += ones[mid] - ones[left] - (mid - left)

    print(count)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
