def prison(n, m, lrli):

    rmin = 10**5
    lmax = 0

    for i in lrli:
        rmin = min(rmin, i[1])
        lmax = max(lmax, i[0])

    return rmin-lmax+1 if rmin >= lmax else 0

def main():
    n, m = map(int, input().split())
    lrli = [list(map(int, input().split()))for i in range(m)]
    print(prison(n, m, lrli))

if __name__ == '__main__':
    main()