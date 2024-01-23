def c170(x, n, plist):

    if n == 1:
        if x - n not in plist:
            return x - n
        else:
            return x + n

    for i in range(n):
        if x-i not in plist:
            return x-i
        elif x+i not in plist:
            return x+i

def main():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        return
    plist = list(map(int, input().split()))
    print(c170(x, n, plist))

if __name__ == '__main__':
    main()