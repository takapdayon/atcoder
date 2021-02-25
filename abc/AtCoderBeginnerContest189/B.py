def b189(n, x, vp):

    ans = 0
    for i, vpi in enumerate(vp):
        ans += vpi[0]*(vpi[1])
        if ans > x*100:
            return i+1
    return -1

n, x = map(int, input().split())
vp = [list(map(int, input().split())) for _ in range(n)]
print(b189(n, x, vp))