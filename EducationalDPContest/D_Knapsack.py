
def knapsack(n, width, wvlist):

    dp = [[0]*(width+1) for i in range(n+1)]

    for i, (w, v) in enumerate(wvlist, start=1):
        for l in range(width + 1):
            if l - w >= 0:
                dp[i][l] = max(dp[i][l], dp[i-1][l-w] + v)
            dp[i][l] = max(dp[i][l], dp[i-1][l])
    return dp[-1][-1]

def main():
    n, width = map(int, input().split())
    wvlist = [map(int, input().split())for i in range(n)]
    print(knapsack(n, width, wvlist))

if __name__ == '__main__':
    main()
