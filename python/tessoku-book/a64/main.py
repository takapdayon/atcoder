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
    n, m = i_map()
    m_len = [ 10 ** 9 ] * (n + 1)
    m_len[1] = 0

    graph = defaultdict(list)
    for _ in range(m):
        a, b, c = i_map()
        graph[a].append([b, c])
        graph[b].append([a, c])

    queue = deque()
    queue.append(1)

    while queue:
        now = queue.popleft()
        # もし行けるノードがより低い値に更新可能だったらqueueに入れて進める
        for to in graph[now]:
            if m_len[to[0]] > to[1] + m_len[now]:
                queue.append(to[0])
                m_len[to[0]] = to[1] + m_len[now]

    for i in range(1, n + 1):
        if m_len[i] == 10 ** 9:
            print(-1)
        else:
            print(m_len[i])

if __name__ == '__main__':
    main()

# テスト: oj t -c 'poetry run python main.py'
# 提出: acc s main.py -- --guess-python-interpreter pypy
# 再帰あるとき:  acc s main.py -- --guess-python-interpreter cpython --language 5055
