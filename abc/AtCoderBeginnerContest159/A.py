def saiki(n):

    if n == 0:
        return 0
    else:
        return n + saiki(n - 1)

def number(n , m):

    ans = saiki(n) + saiki(m) - n - m

    return ans

def main():
    n , m = map(int , input().split())
    print(number(n , m))

if __name__ == '__main__':
    main()