def c176(n, alist):

    ans = 0
    tmp = alist[0]

    for i in alist:
        if tmp <= i:
            tmp = i
            continue
        ans += tmp - i

    return ans

def main():
    n = int(input())
    alist = list(map(int, input().split()))
    print(c176(n, alist))

if __name__ == '__main__':
    main()