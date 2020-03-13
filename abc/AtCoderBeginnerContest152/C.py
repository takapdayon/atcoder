N = int(input())
li = list(map(int,input().split()))
ans = 0
data = N

for i in range(N):
    if data >= li[i]:
        ans += 1
        data = li[i]

print(ans)