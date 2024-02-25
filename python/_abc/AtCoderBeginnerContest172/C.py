def c172(n, m, k, alist, blist):

    ali = [0]*(n + 1)
    bli = [0]*(m + 1)

    for i in range(1, n):
        ali[i + 1] = ali[i] + alist[i]

    for i in range(1, m):
        bli[i + 1] = bli[i] + blist[i]

    

def main():
    n, m, k = map(int, input().split())
    alist = list(map(int, input().split()))
    blist = list(map(int, input().split()))
    print(c172(n, m, k, alist, blist))

if __name__ == '__main__':
    main()