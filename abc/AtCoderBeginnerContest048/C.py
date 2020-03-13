N,x = map(int, input().split())
alist = list(map(int,input().split()))
ans = 0

if alist[0] > x:
    ans += (alist[0] - x)
    alist[0] -= (alist[0] - x)

for al in range(1,N):
    if (alist[al-1]+alist[al]) > x:
        ans += (alist[al-1]+alist[al]) - x
        alist[al] -= (alist[al-1]+alist[al]) - x

print(ans)