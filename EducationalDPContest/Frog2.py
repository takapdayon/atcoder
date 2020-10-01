def chmin(dp, i, a):
    if a < dp[i]:
        dp[i] = a
        return True
    return False

def frog2(n, k, hlist):

    dp = [10**9]*(n)
    dp[0] = 0

    for i in range(n):
        for w in range(i, min(i+k+1, n)):
            chmin(dp, w, dp[i] + abs(hlist[i] - hlist[w]))
    return dp[-1]

def main():
    n, k = map(int, input().split())
    hlist = list(map(int, input().split()))
    print(frog2(n, k, hlist))

if __name__ == '__main__':
    main()