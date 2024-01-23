import itertools

def b187(n, xy):

    ans = 0
    itelist = list(itertools.combinations(range(len(xy)), 2))
    for i, w in itelist:
        yy = xy[w][1] - xy[i][1]
        xx = xy[w][0] - xy[i][0]
        if -1 <= yy/xx <= 1:
            ans += 1
    return ans

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
print(b187(n, xy))