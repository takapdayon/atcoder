import itertools


def c177(n, alist):

    ans = 0
    mod = 10**9+7

    itelist = list(itertools.combinations(range(n), 2))

    for l, r in itelist:
        ans += (alist[l]* alist[r])

    return ans % mod

def main():
    n = int(input())
    alist = list(map(int, input().split()))
    print(c177(n, alist))

if __name__ == '__main__':
    main()