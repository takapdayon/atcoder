from typing import AnyStr


def c207(n, tlr):

    ans = 0

    for i in range(n):
        for w in range(i, n):
            if tlr[i][2] >= tlr[w][1] or tlr[i][1] <= tlr[w][2]:
                ans += 1

    return ans

n = int(input())
tlr = [list(map(int, input().split())) for i in range(n)]
print(c207(n, tlr))
