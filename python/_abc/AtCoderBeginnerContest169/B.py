def b169(n, alist):

    ans = 1
    for i in alist:
        if i == 0:
            return 0

    for i in alist:
        ans *= i
        if ans > 10**18:
            return -1

    return ans

def main():
    n = int(input())
    alist = list(map(int, input().split()))
    print(b169(n, alist))

if __name__ == '__main__':
    main()