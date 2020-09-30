def chmin(dp, i, a):
    if a < dp[i]:
        dp[i] == a
        return True
    return False

def frog(n, hlist):

    dp = [10**5]*(n+1)
    dp[0] = 0

    for i in range(1, n+1):
        chmin(dp, i, hlist[i-1])
        if i > 1:
            chmin(dp, i, hlist[i-2])
    return dp[-1]

def main():
    n = int(input())
    hlist = list(map(int, input().split()))
    print(frog(n, hlist))

if __name__ == '__main__':
    main()