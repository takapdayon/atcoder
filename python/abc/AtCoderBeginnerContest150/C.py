import itertools

def countOrder(n, plist, qlist):

    ans = 0
    p = 0
    q = 0

    irelist = list(itertools.permutations(range(1, n+1), n))

    for index, i in enumerate(irelist):
        if i == plist:
            p = index
        if i == qlist:
            q = index

    ans = abs(p-q)

    return ans

def main():
    n = int(input())
    plist = tuple(map(int, input().split()))
    qlist = tuple(map(int, input().split()))
    print(countOrder(n, plist, qlist))

if __name__ == '__main__':
    main()