N = int(input())
S = str(input())
count = 0
ans = 0

for i in range(N):
    if S[i:i+1] == "I":
        count += 1
        ans = max(ans,count)
    else:
        count -= 1
        ans = max(ans,count)

print(ans)