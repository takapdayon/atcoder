def b184(n, x, s):

    for i in s:
        if i == "x":
            x -= 1 if x != 0 else 0
        else:
            x += 1

    return x

n, x = map(int, input().split())
s = list(str(input()))
print(b184(n, x, s))