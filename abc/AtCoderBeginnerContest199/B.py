def b199(n, al, bl):

    xmi = 0
    xma = 10000

    for i in range(n):
        xmi = max(xmi, al[i])
        xma = min(xma, bl[i])

    ans = xma - xmi + 1

    return ans if ans >= 0 else 0

n = int(input())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
print(b199(n, al, bl))
