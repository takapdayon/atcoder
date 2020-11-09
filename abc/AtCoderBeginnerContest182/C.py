import itertools

def c182(n):

    ans = 1000

    itelist = list(itertools.product(range(0, 2), repeat=len(n)))

    for i in itelist:
        count = ""
        for w, nn in zip(i, n):
            if w == 1:
                count += nn
        if count and int(count) % 3 == 0:
            ans = min(ans, len(n) - len(count))

    return ans if ans != 1000 else -1

n = list(str(input()))
print(c182(n))
