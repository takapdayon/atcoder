import itertools

def takoyaki_festival2019(n, dli):

    ans = 0
    itelist = list(itertools.combinations(range(n), 2))

    for i, k in itelist:
        ans += dli[i]*dli[k]

    return ans

def main():
    n = int(input())
    dli = list(map(int, input().split()))
    print(takoyaki_festival2019(n, dli))

if __name__ == '__main__':
    main()