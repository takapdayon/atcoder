def b207(a, b, c, d):

    ans = 0
    blue = a
    red = 0

    if b >= c * d:
        return -1

    while True:
        if red * d >= blue:
            break
        blue += b
        red += c
        ans += 1

    return ans

a, b, c, d = map(int, input().split())
print(b207(a, b, c, d))
