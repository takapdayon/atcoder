def b186(n, w, alist):

    amin = 100
    for i in alist:
        amin = min(amin, min(i))
    ans = 0
    for i in alist:
        for w in i:
            ans += w - amin

    return ans

n, w = map(int, input().split())
alist = [list(map(int, input().split())) for _ in range(n)]
print(b186(n, w, alist))