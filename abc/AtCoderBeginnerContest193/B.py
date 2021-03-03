def b193(n, apxl):

    ans = 10**9 + 100
    time = 0
    for apx in apxl:
        if apx[2] - apx[0] > 0:
            ans = min(ans, apx[1])

    if ans == 10**9 + 100:
        return -1
    return ans

n = int(input())
apxl = [list(map(int, input().split())) for _ in range(n)]
print(b193(n, apxl))