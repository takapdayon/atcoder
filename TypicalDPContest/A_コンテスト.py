def contest(n, plist):

    ans = 0
    dp = [[False]*(sum(plist)+1) for i in range(n+1)]
    dp[0][0] = True

    for i, p in enumerate(plist, start=1):
        for w in range(sum(plist)+1):
            if w - p >= 0:
                if dp[i-1][w-p]:
                    dp[i][w] = True
            if dp[i-1][w]:
                dp[i][w] = True

    ans = dp[n].count(True)

    return ans

def main():
    n = int(input())
    plist = list(map(int, input().split()))
    print(contest(n, plist))

if __name__ == '__main__':
    main()
