import sys
sys.setrecursionlimit(10000)

from functools import lru_cache

@lru_cache(maxsize=None)
def mem(i):
    result = []
    for ab in ablist:
        if ab[0] == i:
            result.append(ab[1])
    return result

def tmp(i):

    stack = mem(i)
    stack = [w for w in stack if not is_visited[w - 1]]

    if not stack:
        return 0

    result = 0

    for s in stack:
        is_visited[s - 1] = True

    for s in stack:
        result += tmp(s)

    return len(stack) + result

n, m = map(int, input().split())
ablist = [list(map(int, input().split())) for _ in range(m)]
ans = n

for i in range(1, n + 1):
    is_visited = [False] * n
    is_visited[i - 1] = True
    ans += tmp(i)

print(ans)