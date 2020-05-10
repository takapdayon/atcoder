def balance(n, wli):

    ans = 10**9

    for i in range(n):
        ans = min(ans, abs(int(sum(wli[:i]))-int(sum(wli[i:]))))

    return ans
def main():
    n = int(input())
    wli = list(map(int, input().split()))
    print(balance(n, wli))

if __name__ == '__main__':
    main()