def knapsack(n, width, wvlist):

    max_v = 10**5 + 100
    ans = 0
    dp = [[10**9+1]*(max_v) for i in range(n+1)]
    dp[0][0] = 0

    for i, (w, v) in enumerate(wvlist, start=1):
        for rav in range(max_v):
            if rav - v >= 0:
                dp[i][rav] = min(dp[i][rav], dp[i-1][rav-v] + w)
            dp[i][rav] = min(dp[i][rav], dp[i-1][rav])

    for i, res in enumerate(dp[n]):
        if res <= width:
            ans = i

    return ans

def main():
    n, width = map(int, input().split())
    wvlist = [map(int, input().split())for i in range(n)]
    print(knapsack(n, width, wvlist))

if __name__ == '__main__':
    main()
