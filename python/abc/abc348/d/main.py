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
from atcoder.dsu import DSU

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
    H, W = i_map()
    arows = s_row_list(H)
    N = i_input()
    rcerows = i_row_list(N)
    uf = DSU(N + 2)

    es = {}
    comb = {}
    for i, (r, c, e) in enumerate(rcerows):
        es[(r - 1, c - 1)] = e
        comb[(r - 1, c - 1)] = i

    start = []
    for h in range(H):
        for w in range(W):
            if arows[h][w] == 'S':
                start = [h, w]

    # スタートの位置にある薬とSをmerge
    uf.merge(N, comb.get((start[0], start[1]), N))

    queue = deque()
    queue.append((start, 0))

    visited_medi = {}

    while queue:
        visited = [[False] * W for _ in range(H)]
        (ch, cw), e = queue.popleft()
        m_q = deque()
        m_q.append(((ch, cw), e))

        while m_q:
            (mch, mcw), m_e = m_q.popleft()
            if es.get((mch, mcw)) and not visited_medi.get((mch, mcw), False):
                queue.append(((mch, mcw), es.get((mch, mcw))))
                visited_medi[(mch, mcw)] = True
                uf.merge(comb.get((ch, cw)), comb.get((mch, mcw)))

            if arows[mch][mcw] == 'T':
                uf.merge(comb.get((ch, cw)), N + 1)

            if m_e == 0:
                continue

            # 行ける場所探し
            for h_s, w_s in zip([1, 0, -1, 0], [0, -1, 0, 1]):
                nh = mch + h_s
                nw = mcw + w_s
                if nh >= H or nh < 0:
                    continue
                if nw >= W or nw < 0:
                    continue
                if arows[nh][nw] == '#':
                    continue
                if visited[nh][nw]:
                    continue
                visited[nh][nw] = True
                m_q.append(((nh, nw), m_e - 1))

    print(uf.same(N, N + 1) and 'Yes' or 'No')

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
