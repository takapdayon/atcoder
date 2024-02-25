def splittingplie(n , a):

    ans = 10**18
    allsum = int(sum(a))
    asum = 0

    for i in range(n - 1):
        asum += a[i]
        rldifference = abs(allsum - asum*2)
        ans = min(ans , rldifference)

    return ans

def main():
    n = int(input())
    a = list(map(int , input().split()))
    print(splittingplie(n , a))

if __name__ == '__main__':
    main()