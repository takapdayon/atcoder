def c203(n, k, ablist):

    ans = 0
    ablist = sorted(ablist, key=lambda x: x[0])
    before = 0

    for ab in ablist:
        if ab[0] == before:
            k += ab[1]
            continue

        if (k+ans) < ab[0]:
            return ans+k

        k = ((ans + k) - ab[0]) + ab[1]
        ans = ab[0]
        before = ab[0]

    return ans+k

n, k = map(int, input().split())
ablist = [list(map(int, input().split())) for i in range(n)]
print(c203(n, k, ablist))
