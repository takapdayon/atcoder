import math

def c198(r, x, y):
    sqrt = math.sqrt(((0 - x)**2)+((0 - y)**2))
    if sqrt < r:
        return 2
    ans = math.ceil(sqrt / r)
    return ans

r, x, y = map(int, input().split())
print(c198(r, x, y))
