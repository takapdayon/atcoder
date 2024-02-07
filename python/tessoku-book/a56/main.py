import sys, re
from math import ceil, floor, sqrt, pi, gcd, lcm, factorial, atan, degrees
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext

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
    '''
    rolling hashに関してかつっぱさんのyoutubeがとても分かりやすかった
    https://www.youtube.com/watch?v=Yc37rKy2-tQ

    注意はMODの大きさで衝突確率が変動することと、絶対に衝突させたくない場合は一致した際に文字列も確認すること
    今度DPでも解いてみたい。
    '''
    n, q = i_map()
    s = s_input()
    queries = i_row_list(q)
    strings = [0]
    for i in range(n):
        hash_v = (strings[i] * 100 + ord(s[i])) % MOD
        strings.append(hash_v)

    for a, b, c, d in queries:
        hash_ab = strings[b] - (strings[a - 1] * pow(100, b - a + 1, MOD)) % MOD
        if hash_ab < 0:
            hash_ab += MOD
        hash_cd = strings[d] - (strings[c - 1] * pow(100, d - c + 1, MOD)) % MOD
        if hash_cd < 0:
            hash_cd += MOD
        if hash_ab == hash_cd:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()

# テスト: oj t -c 'python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
