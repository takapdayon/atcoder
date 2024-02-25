def c190(n, m, abl, k, cdl):

    ans = 0

    return ans

n, m = map(int, input().split())
abl = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
cdl = [list(map(int, input().split())) for _ in range(k)]
print(c190(n, m, abl, k, cdl))
