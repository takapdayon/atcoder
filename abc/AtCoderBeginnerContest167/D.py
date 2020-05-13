def d167(n, k, ali):

    ncount = [False]*n
    nncount = [0]*n
    ans = 0
    s = 0
    waru = 0
    trueans = 0

    while True:
        if ncount[s-1]:
            waru = ans-nncount[s-1]
            break
        ncount[s-1] = True
        nncount[s-1] = ans
        ans += 1
        s = ali[s-1]

    trueans = (k-nncount[s-1])%waru

    for i in range(trueans):
        s = ali[s-1]

    return s

def main():
    n, k = map(int, input().split())
    ali = list(map(int, input().split()))
    print(d167(n, k, ali))
if __name__ == '__main__':
    main()