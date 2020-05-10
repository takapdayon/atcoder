def typical_stairs(n, m, ali):

    mod = 10**9+7
    flag = [True]*(n+1)
    for i in ali:
        flag[i] = False

    dp = [0]*(n+1)
    dp[0] = 1

    for i in range(1, n+1):
        if not flag[i]:
            continue
        dp[i] = dp[i-2] + dp[i-1]
        dp[i] %= mod

    return dp[i]

def main():
    n, m = map(int, input().split())
    ali = [int(input())for i in range(m)]
    print(typical_stairs(n, m, ali))

if __name__ == '__main__':
    main()