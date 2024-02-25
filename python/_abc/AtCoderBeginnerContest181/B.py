def b181(n, ablist):

    nli = [0]*(10**6 + 1)
    ans = 0

    for i in range(1, len(nli)):
        nli[i] = nli[i - 1] + i

    for a, b in ablist:
        ans += nli[b] - nli[a - 1]

    return ans

n = int(input())
ablist = [list(map(int, input().split()))for i in range(n)]
print(b181(n, ablist))