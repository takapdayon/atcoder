def vacation(n, abclist):

    dp = [[0, 0, 0] for i in range(n+1)]

    for i in range(1, n+1):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2])+abclist[i-1][0]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2])+abclist[i-1][1]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1])+abclist[i-1][2]
    return max(dp[-1])

def main():
    n = int(input())
    abclist = [list(map(int, input().split()))for i in range(n)]
    print(vacation(n, abclist))

if __name__ == '__main__':
    main()