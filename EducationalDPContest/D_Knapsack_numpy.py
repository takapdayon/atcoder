import numpy as np

def knapsack(n, width, wvlist):

    dp = np.zeros(width+1, dtype=int)

    for i, (w, v) in enumerate(wvlist, start=1):
        dp[w:] = np.maximum(dp[w:], dp[:-w] + v)

    return dp.max()

def main():
    n, width = map(int, input().split())
    wvlist = [map(int, input().split())for i in range(n)]
    print(knapsack(n, width, wvlist))

if __name__ == '__main__':
    main()
