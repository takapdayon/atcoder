import itertools

def c185(l):

    r = 1
    for i in range(1, 12):
        r *= l - i
        r //= i

    return int(r)

l = int(input())
print(c185(l))