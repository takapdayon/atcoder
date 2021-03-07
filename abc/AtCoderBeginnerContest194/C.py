from collections import defaultdict

def c194(n, al):

    d = defaultdict(int)
    for i in al:
        d[str(i)] += 1

    ans = 0

    for i in range(-200, 201):
        for w in range(i, 201):
            if i == w:
                try:
                    ans += d[str(i)]* (d[str(w)]-1) * ((i - w) ** 2)
                except:
                    pass
                continue
            try:
                ans += d[str(i)]*d[str(w)] * ((i - w) ** 2)
            except:
                pass

    return ans

n = int(input())
al = list(map(int, input().split()))
print(c194(n, al))
