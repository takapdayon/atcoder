def countave(n , a):
    ans = 100000000000000

    for i in range(2):
        kei = 0
        forans = 0
        for w in range(n):
            if (w + i) % 2:
                if kei + int(a[w]) > -1:
                    forans += abs(kei + int(a[w])) + 1
                    kei = -1
                else:
                    kei += int(a[w])
            else:
                if kei + int(a[w]) < 1:
                    forans += abs(kei + int(a[w])) + 1
                    kei = 1
                else:
                    kei += int(a[w])

        ans = min(ans , forans)

    return ans

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(countave(n , a))

if __name__ == '__main__':
    main()
