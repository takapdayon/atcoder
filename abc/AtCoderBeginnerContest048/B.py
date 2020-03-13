a , b , x = map(int, input().split())
ans = b // x

if a == 0:
    print(ans + 1)
else:
    print(ans - (a - 1) // x)
