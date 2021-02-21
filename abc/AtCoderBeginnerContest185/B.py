def b185(N, m, t, ab):

    time = 0
    n = N
    for a, b in ab:
        if n - (a - time) <= 0:
            return "No"
        n = n - (a - time) + (b - a) if n - (a - time) + (b - a) <= N else N
        time = b

    return "No" if n - (t - time) <= 0 else "Yes"

N, m, t = map(int, input().split())
ab = [map(int, input().split()) for _ in range(m)]
print(b185(N, m, t, ab))