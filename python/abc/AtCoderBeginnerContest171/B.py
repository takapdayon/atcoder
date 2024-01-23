def b171(n, k, plist):

    plist.sort()

    return sum(plist[:k])

def main():
    n, k = map(int, input().split())
    plist = list(map(int, input().split()))
    print(b171(n, k, plist))

if __name__ == '__main__':
    main()