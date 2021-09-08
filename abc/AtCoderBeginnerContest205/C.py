def c205(a, b, c):

    if c % 2 == 0:
        if abs(a) < abs(b):
            return "<"
        elif abs(a) > abs(b):
            return ">"
        else:
            return "="

    if a < b:
        return "<"
    if a > b:
        return ">"
    return "="

a, b, c = map(int, input().split())
print(c205(a, b, c))
