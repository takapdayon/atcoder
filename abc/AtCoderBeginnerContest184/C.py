import itertools

def c183(n, k, tlist):

    ans = 0

    irelist = list(itertools.permutations(range(2, n + 1), n - 1))

    for ire in irelist:
        count = 0
        nn = ire[0] - 1
        rr = ire[-1] - 1
        count += tlist[0][nn]
        count += tlist[rr][0]
        for index in range(len(ire) - 1):
            i = ire[index] - 1
            j = ire[index + 1] - 1
            count += tlist[i][j]

        if count == k:
            ans += 1

    return ans

n, k = map(int, input().split())
tlist = [list(map(int, input().split())) for i in range(n)]
print(c183(n, k, tlist))
