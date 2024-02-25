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
    line = input().split()
    N = int(line[0])
    M = int(line[1])
    eps = float(line[2])
    fields = []
    for _ in range(M):
        line = input().split()
        ps = []
        for i in range(int(line[0])):
            ps.append((int(line[2*i+1]), int(line[2*i+2])))
        fields.append(ps)

    # drill every square
    has_oil = []
    for i in range(N):
        for j in range(N):
            print("q 1 {} {}".format(i, j))
            resp = input()
            if resp != "0":
                has_oil.append((i, j))

    print("a {} {}".format(len(has_oil), ' '.join(map(lambda x: "{} {}".format(x[0], x[1]), has_oil))))
    resp = input()
    assert resp == "1"


if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055

'''
やりたいこと:
コストをできる限り少なく、すべてのテトリスの座標を暴きたい


考えること:
テトリスの素材がある。それがN*Nのマスどこかに埋められている(重複する可能性もある)
向きとサイズは決まっている。

> マス(i,j) に対して、石油埋蔵量 v(i,j) を、そのマスを含む油田の数として定義する
つまり
'''
