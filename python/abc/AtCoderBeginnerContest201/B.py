def b201(n, stlist):

    li = sorted(stlist, reverse=True, key=lambda x: int(x[1]))

    return li[1][0]

n = int(input())
stlist = [list(map(str, input().split())) for i in range(n)]
print(b201(n, stlist))
