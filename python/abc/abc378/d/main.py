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

NH = [1, 0, -1, 0]
NW = [0, -1, 0, 1]
TANOMU = list(zip(NH, NW))


def dfs(node, visited, k, H, W, SHW):
    if k == 0:
        return 1

    visited[node[0]][node[1]] = True

    tmp = 0
    for nh, nw in TANOMU:
        nhi, nwi = nh + node[0], nw + node[1]
        if nhi < 0 or nwi < 0 or nhi >= H or nwi >= W:
            continue
        if SHW[nhi][nwi] == '#':
            continue
        if visited[nhi][nwi]:
            continue
        tmp += dfs((nhi, nwi), visited, k - 1, H, W, SHW)

    visited[node[0]][node[1]] = False

    return tmp

def main():
    H, W, K = i_map()
    SHW = s_row_list(H)

    # BFSして、個数がKの時に+1
    result = 0
    for h in range(H):
        for w in range(W):
            if SHW[h][w] == '#':
                continue
            visited = [[False] * W for _ in range(H)]
            result += dfs((h, w), visited, K, H, W, SHW)

            # queue = deque()
            # queue.append(((h, w), 0, visited))
            # while queue:
            #     now, idx, vtd = queue.popleft()
            #     if idx == K:
            #         result += 1
            #     vtd[now[0]][now[1]] = True
            #     for nh, nw in zip([1, 0, -1, 0], [0, -1, 0, 1]):
            #         nhi, nwi = nh + now[0], nw + now[1]
            #         if nhi < 0 or nwi < 0 or nhi >= H or nwi >= W:
            #             continue
            #         if SHW[nhi][nwi] == '#':
            #             continue
            #         if vtd[nhi][nwi]:
            #             continue
            #         queue.append(((nhi, nwi), idx + 1, [i[:] for i in vtd]))

    print(result)

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
