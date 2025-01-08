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
    K = i_input()
    S = s_input()
    T = s_input()
    s_queue = deque(S)
    t_queue = deque(T)

    if S == T:
        print("Yes")
        return

    if abs(len(S) - len(T)) > 1:
        print("No")
        return

    if len(S) == len(T):
        # 削除、挿入はない
        flag = False
        while len(s_queue):
            p_s = s_queue.popleft()
            p_t = t_queue.popleft()
            if p_s == p_t:
                continue
            elif flag:
                print("No")
                return
            else:
                flag = True
        print("Yes")
        return

    prev_s = ''
    prev_t = ''
    flag = False
    if len(s_queue) > len(t_queue):
        # 削除
        while len(s_queue):
            p_s = s_queue.popleft()
            if prev_t:
                if prev_t == p_s:
                    prev_t = ''
                    continue
                else:
                    print('No')
                    return
            if not len(t_queue):
                print("Yes")
                return
            p_t = t_queue.popleft()
            if p_s == p_t:
                continue
            elif flag:
                print("No")
                return
            else:
                flag = True
                prev_t = p_t
    else:
        # 挿入
        while len(t_queue):
            p_t = t_queue.popleft()
            if prev_s:
                if prev_s == p_t:
                    prev_s = ''
                    continue
                else:
                    print('No')
                    return
            if not len(s_queue):
                print("Yes")
                return
            p_s = s_queue.popleft()
            if p_s == p_t:
                continue
            elif flag:
                print("No")
                return
            else:
                flag = True
                prev_s = p_s
    print("Yes")

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
