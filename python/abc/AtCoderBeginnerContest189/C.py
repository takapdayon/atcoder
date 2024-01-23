def c189(n, al):

    ans = 0
    for i in range(len(al)):
        ans = max(ans, al[i])
        minimum = al[i]
        for w in range(i+1, len(al)):
            minimum = min(minimum, al[w])
            tmp = minimum * (w - i + 1)
            ans = max(ans, tmp)
    return ans

n = int(input())
al = list(map(int, input().split()))
print(c189(n, al))
