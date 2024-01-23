def b180(n, xlist):

    mahat = 0
    yuku = 0
    tyobyi = 0

    for i in xlist:
        mahat += abs(i)
        yuku += abs(i)**2
        tyobyi = max(tyobyi, abs(i))

    yuku **= 0.5

    return mahat, yuku, tyobyi

n = int(input())
xlist = map(int, input().split())
mahat, yuku, tyobyi = b180(n, xlist)

print(mahat)
print(yuku)
print(tyobyi)