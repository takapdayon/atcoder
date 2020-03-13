def hsi(n , m):

    ans = ((1900 * m) + (100 * (n - m))) * (2**m)
    return ans

def main():
    n, m = map(int, input().split())
    print(hsi(n , m))

if __name__ == '__main__':
    main()