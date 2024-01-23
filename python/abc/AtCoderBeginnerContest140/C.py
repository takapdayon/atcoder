def lower(n, hli):

    hli.reverse()
    ans = 0
    count = 0

    for i in range(n-1):
        if hli[i] <= hli[i+1]:
            count += 1
            ans = max(ans, count)
        else:
            ans = max(ans, count)
            count = 0

    return ans

def main():
    n = int(input())
    hli = list(map(int, input().split()))
    print(lower(n, hli))

if __name__ == '__main__':
    main()