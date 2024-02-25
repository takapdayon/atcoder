def a184(a, b, c, d):

    return a*d - b*c

a, b = map(int, input().split())
c, d = map(int, input().split())
print(a184(a, b, c, d))