def b194(n, abl):
    a = 10**8
    b = 10**8
    num = 0
    count = 0
    pl = 10**8

    for ab in abl:
        pl = min(pl, ab[0] + ab[1])

    for i, ab in enumerate(abl):
        if a >= ab[0]:
            num = i
            a = ab[0]

    for ab in abl:
        if ab[0] == a:
            count += 1

    for i, ab in enumerate(abl):
        if b >= ab[1]:
            if i == num and count == 1:
                continue
            b = ab[1]

    return min(pl, max(a, b))

n = int(input())
abl = [list(map(int, input().split())) for _ in range(n)]
print(b194(n, abl))