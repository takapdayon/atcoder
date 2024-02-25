def b203(n, k):

    ans = 0

    for nn in range(1, n+1):
        for kk in range(1, k+1):
            ans += nn*100 + kk

    return ans

n, k = map(int, input().split())
print(b203(n, k))
