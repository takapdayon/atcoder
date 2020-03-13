def tasu(x):
    return x / 2 * (x + 1)

def kitaiti(n , k , p):

    ans = 0
    count = 0
    kitai = [0]*n
    kitaisum = [0]*n
    mod = 10**9+7

    for i in range(n):
        kitai[i] = tasu(p[i]) / p[i]

    for i in range(n):
        if i == 0:
            kitaisum[i] += kitai[i]
        else:
            kitaisum[i] += kitai[i] + kitaisum[i-1]

    for i in range(n - k + 1):

        ans = max(ans , (kitaisum[i + k - 1] - kitaisum[i-1]) if i != 0 else kitaisum[i + k - 1])

    return ans

def main():
    n , k = map(int , input().split())
    p = list(map(int,input().split()))
    print(kitaiti(n , k , p))

if __name__ == '__main__':
    main()