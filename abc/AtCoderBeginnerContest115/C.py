def cChristmas(n, k, hl):


    hl.sort()
    ans = 10**10

    for i in range(n-k+1):
        ans = min(ans, hl[i+k-1]-hl[i])

    return ans

def main():
    n, k = map(int, input().split())
    hl = [int(input()) for i in range(n)]
    print(cChristmas(n, k, hl))

if __name__ == '__main__':
    main()
