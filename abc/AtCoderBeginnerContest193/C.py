def c193(n):

    ans = n
    mlist = set()
    10000000000
    for i in range(1, n+1):
        if i == 1:
            continue
        if i ** 2 > n:
            break
        count = 2
        while True:
            if i ** count <= n:
                mlist.add(i**count)
            else:
                break
            count += 1

    return n - len(mlist)

n = int(input())
print(c193(n))
