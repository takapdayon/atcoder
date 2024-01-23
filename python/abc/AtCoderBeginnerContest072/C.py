def together(n , a):

    listans = [0]*(10**5+2)

    for i in range(n):
        listans[a[i] - 1] += 1
        listans[a[i]] += 1
        listans[a[i] + 1] += 1

    return max(listans)


def main():
    n = int(input())
    a = list(map(int,input().split()))
    print(together(n , a))

if __name__ == '__main__':
    main()