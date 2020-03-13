N = int(input())
count = [1]*(N+1)
ans = 1
mod = 10**9+7

for i in range(2,N+1):
    wari = i
    for w in range(2,i+1):
        while wari % w == 0:
            count[w] += 1
            wari /= w

for i in range(N+1):
    ans *= count[i]

print(ans % mod)