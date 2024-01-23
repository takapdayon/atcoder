x, y = map(int, input().split())
a = {0, 1, 2}
if x == y:
    print(x)
else:
    print(*(a - {x, y}))