a,b = map(int, input().split())
ans = ""

for i in range(max(a,b)):
    ans += (str(min(a,b)))
print(ans)