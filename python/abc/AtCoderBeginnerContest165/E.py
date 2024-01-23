H , A = map(int, input().split())
Clist = [input().split() for i in range(H)]


def hanbun(x):
    if x%2 == 0:
        return x/2 , x/2
    else:
        return x//2 , (x//2) + 1

print((H/2) - 1)

1,000,000,000,000

1,099,511,627,775

100