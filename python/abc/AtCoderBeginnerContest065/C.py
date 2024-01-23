import math

def reconclied(n , m):

    ans = 0
    mod = 10**9 + 7

    if n == m:
        ans = 2 * (math.factorial(n) * math.factorial(m))

    elif abs(n - m) == 1:
        ans = (math.factorial(n) * math.factorial(m))

    return ans % mod

def main():
    n , m = map(int , input().split())
    print(reconclied(n , m))

if __name__ == '__main__':
    main()