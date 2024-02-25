def makerectangle(n , a):

    listmax = []
    a.sort(reverse=True)
    for i in range(n):
        if len(a) > i + 1 and a[i] == a[i + 1] and listmax.count(a[i]) == 0:
            if len(a) > i + 3 and a[i] == a[i + 3] and len(listmax) == 0:
                return a[i] * a[i]
            else:
                listmax.append(a[i])
        if len(listmax) > 1:
            return listmax[0] * listmax[1]
    return 0


def main():
    n = int(input())
    a = list(map(int,input().split()))
    print(makerectangle(n , a))

if __name__ == '__main__':
    main()