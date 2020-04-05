def Candles(n , k , xl):

    ans = 10**9

    for i in range(n - k + 1):
        lr = min(abs(xl[i]) + abs(xl[i] - xl[i + k - 1]) , abs(xl[i + k - 1]) + abs(xl[i + k - 1] - xl[i]))
        ans = min(ans , lr)

    return ans

def main():
    n , k = map(int , input().split())
    xl = list(map(int , input().split()))
    print(Candles(n , k , xl))

if __name__ == '__main__':
    main()