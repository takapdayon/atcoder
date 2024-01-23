def c187(n, slist):
    slist = list(set(slist))
    ss = set()
    for s in slist:
        s = s.lstrip('!')
        if s in ss:
            return s
        ss.add(s)

    return 'satisfiable'

n = int(input())
slist = [str(input()) for _ in range(n)]
print(c187(n, slist))
